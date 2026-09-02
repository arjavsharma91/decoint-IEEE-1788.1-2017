from dataclasses import dataclass
from gmpy2 import mpfr, RoundUp, RoundDown, context, get_context, is_nan, is_infinite, next_below
import re
from typing import Tuple

ctx = get_context()
ctx.precision = 53
ctx.emin = -1074
ctx.emax = 1024

BOX_REGEX = re.compile(r"^\[\s*([^,;\]]+?)\s*(?:[,;]\s*([^,;\]]*?))?\s*\]$")
UNC_REGEX = re.compile(r"^([^?]+)\?(.*)$")

Number = mpfr
@dataclass(frozen = True)
class Interval:
    lo: Number = Number('-inf')
    hi: Number = Number('inf')

    def __post_init__(self):

        if isinstance(self.lo, str):
            parsed_interval = Interval.from_string(self.lo)
            if not (is_nan(parsed_interval.lo) or is_nan(parsed_interval.hi)):
                object.__setattr__(self, "lo", parsed_interval.lo)
                object.__setattr__(self, "hi", parsed_interval.hi)
            else:
                pass
                
        
        with context(get_context(), round=RoundDown):
            lo = Number(self.lo)
        with context(get_context(), round=RoundUp):
            hi = Number(self.hi)

        if lo > hi:
            object.__setattr__(self, "lo", Number('inf'))
            object.__setattr__(self, "hi", Number('-inf'))

        if is_nan(lo) or is_nan(hi):
            object.__setattr__(self, "lo", Number('NaN'))
            object.__setattr__(self, "hi", Number('NaN'))
        
        elif lo == Number('-inf') and hi == Number('-inf'):
            object.__setattr__(self, "lo", Number('NaN'))
            object.__setattr__(self, "hi", Number('NaN'))
        
        elif lo == Number('inf') and hi == Number('inf'):
            object.__setattr__(self, "lo", Number('NaN'))
            object.__setattr__(self, "hi", Number('NaN'))

        else:
            object.__setattr__(self, "lo", lo)
            object.__setattr__(self, "hi", hi)

    @classmethod
    def empty(cls):
        return cls(Number('inf'), Number('-inf'))
    @classmethod
    def entire(cls):
        return cls(Number('-inf'), Number('inf'))

    @classmethod
    def _coerce(cls, value):
        if isinstance(value, cls):
            return value
        if isinstance(value, str):
            return cls.from_string(value)
        if hasattr(value, "interval"):
            return value.interval
        return cls(value, value)

    @classmethod
    def from_string(cls, s: str):
        content = s.strip()
        content_compact = "".join(content.split()).lower()

        if content_compact in ("[]", "[empty]"):
            return cls.empty()
        if content_compact in ("[entire]", "[,]"):
            return cls(Number('-inf'), Number('inf'))

        box_match = BOX_REGEX.match(content)
        if box_match:
            left, right = box_match.groups()
            if right is None:
                lo = cls._parse_bound(left, round_up = False)
                hi = cls._parse_bound(left, round_up = True)
            else:
                lo = cls._parse_bound(left, round_up = False)
                hi = cls._parse_bound(right, round_up = True)
            return cls(lo, hi)

        unc_match = UNC_REGEX.match(content)
        if unc_match:
            lo, hi = cls._parse_uncertainty(content)
            return cls(lo, hi)

        return Interval(Number('nan'), Number('nan'))

    @classmethod 
    def _parse_bound(cls, s: str, round_up: bool):
        s_clean = s.strip() if s else ""
        s_lower = s_clean.lower()
        if not s_clean:
            return Number('inf') if round_up else Number('-inf')
        if s_lower in ('inf', '+inf', 'infinity', '+infinity'):
            return Number('inf')
        if s_lower in ('-inf', '-infinity'):
            return Number('-inf')

        target_round = RoundUp if round_up else RoundDown
        
        with context(get_context(), round = target_round):
            if '/' in s_clean:
                parts = s_clean.split('/')
                if len(parts) == 2:
                    return Number(parts[0]) / Number(parts[1])
        
            return Number(s_clean)
    
    @classmethod
    def _parse_uncertainty(cls, text: str):
        if "??" in text:
            if text.lower().endswith("??u"):
                center_str = text.split("??")[0]
                lo = cls._parse_bound(center_str, round_up = False)
                return lo, Number('inf')
            elif text.lower().endswith("??d"):
                center_str = text.split("??")[0]
                hi = cls._parse_bound(center_str, round_up = True)
                return Number('-inf'), hi
            else:
                return Number('-inf'), Number('inf')

        match = UNC_REGEX.match(text)
        if not match:
            raise ValueError("Malformed Uncertainty Syntax")

        center_str, unc_str = match.groups()
        center_str = center_str.strip()
        unc_str = unc_str.strip() if unc_str else ""
        unc_str_lower = unc_str.lower()

        dec_digits = 0
        check_str = center_str.lower().lstrip('+-')
        if '.' in center_str and not check_str.startswith('0x'):
            dec_digits = len(center_str.split('.')[1])

        # DIRECTION FIX 1: Detect 'u' and 'd' flags, then strip them so 
        # "5ue-5" becomes "5e-5" for clean exponent splitting.
        is_upper_only = 'u' in unc_str_lower
        is_lower_only = 'd' in unc_str_lower
        if is_upper_only:
            unc_str_lower = unc_str_lower.replace('u', '')
        if is_lower_only:
            unc_str_lower = unc_str_lower.replace('d', '')

        unc_str_lower = unc_str_lower.strip()

        # --- UPPER BOUND (hi) ---
        if is_lower_only:
            # DIRECTION FIX 2: If 'd' was present, upper bound is locked to the center value 
            # scaled by the exponent (e.g., 2.5 * 10^-5). No tolerance is added.
            with context(get_context(), round = RoundUp):
                hi = Number(center_str)
                if 'e' in unc_str_lower:
                    _, exp_part = unc_str_lower.split('e')
                    scale_factor = Number(10) ** int(exp_part)
                    hi = hi * scale_factor
        else:
            # Standard upper bound (adds tolerance + center scaled by exponent)
            with context(get_context(), round = RoundUp):
                mid_hi = Number(center_str)
                if not unc_str_lower:
                    tol_hi = Number('0.5') * (Number(10) ** (-dec_digits))
                elif 'e' in unc_str_lower:
                    unc_digits, exp_part = unc_str_lower.split('e')
                    u_val = Number(unc_digits) if unc_digits else Number('0.5')
                    base_tol = u_val * (Number(10) ** (-dec_digits))
                    scale_factor = Number(10) ** int(exp_part)
                    mid_hi = mid_hi * scale_factor
                    tol_hi = base_tol * scale_factor
                else:
                    tol_hi = Number(unc_str_lower) * (Number(10) ** (-dec_digits))

                hi = mid_hi + tol_hi

        # --- LOWER BOUND (lo) ---
        if is_upper_only:
            # DIRECTION FIX 3: If 'u' was present, lower bound is locked to the center value 
            # scaled by the exponent (e.g., 2.5 * 10^-5). No tolerance is subtracted.
            with context(get_context(), round = RoundDown):
                mid_lo = Number(center_str)
                if 'e' in unc_str_lower:
                    _, exp_part = unc_str_lower.split('e')
                    scale_factor = (Number(10) ** int(exp_part))
                    mid_lo = mid_lo * scale_factor
                lo = mid_lo
        else:
            # Standard lower bound (subtracts tolerance)
            with context(get_context(), round = RoundUp):
                if not unc_str_lower:
                    tol_lo = Number('0.5') * (Number(10) ** (-dec_digits))
                elif 'e' in unc_str_lower:
                    unc_digits, exp_part = unc_str_lower.split('e')
                    u_val = Number(unc_digits) if unc_digits else Number('0.5')
                    base_tol = u_val * (Number(10) ** (-dec_digits))
                    scale_factor = Number(10) ** int(exp_part)
                    tol_lo = base_tol * scale_factor
                else:
                    tol_lo = Number(unc_str_lower) * (Number(10) ** (-dec_digits))

            with context(get_context(), round = RoundDown):
                mid_lo = Number(center_str)
                if 'e' in unc_str_lower:
                    _, exp_part = unc_str_lower.split('e')
                    scale_factor = Number(10) ** int(exp_part)
                    mid_lo = mid_lo * scale_factor

                lo = mid_lo - tol_lo
        
        return lo, hi
            
        
    
    @property
    def is_common(self):
        if not is_nan(self.lo) and self.is_bounded and not self.is_empty:
            return True
        return False
    
    @property
    def is_empty(self):
        return self.lo > self.hi
    
    @property
    def is_entire(self):
        return not self.is_empty and self.lo == Number('-inf') and self.hi == Number('inf')
    
    @property
    def is_bounded(self):
        return not self.is_empty and self.lo != Number('-inf') and self.hi != Number('inf')

    @property
    def is_singleton(self):
        return not self.is_empty and self.lo == self.hi
    
    @property
    def width(self):
        if self.is_empty:
            return Number('nan')
        if not self.is_bounded:
            return Number('inf')
        with context(get_context()) as ctx:
            ctx.round = RoundUp
            return self.hi - self.lo
    
    @property
    def radius(self):
        if self.is_empty:
            return Number('nan')
        if not self.is_bounded:
            return Number('inf')

        m = self.midpoint
        with context(get_context(), round = RoundUp):
            d_lo = m - self.lo
            d_hi = self.hi - m
            return max(d_lo, d_hi)

    @property
    def midpoint(self):
        if self.is_empty:
            return Number("nan")
        lo, hi = self.lo, self.hi
        if self.is_entire or (is_infinite(lo) and is_infinite(hi)):
            return Number(0)
        if is_infinite(lo):
            return Number(next_below(Number("-inf")))
        if is_infinite(hi):
            return Number(next_below(Number("inf")))
        return (lo / 2) + (hi / 2)

    @property
    def magnitude(self):
        if self.is_empty:
            return Number("nan")
        return max(abs(self.lo), abs(self.hi))
    @property
    def mignitude(self):
        if self.is_empty:
            return Number("nan")
        if self.contains(0):
            return Number(0)
        
        return min(abs(self.lo), abs(self.hi))
    
    def contains(self, x):
        try:
            x = Number(x)
        except Exception:
            return False
        if self.is_empty:
            return False
        if is_infinite(x):
            return False
        return self.lo <= x <= self.hi

    def subset(self, other):
        if not isinstance(other, Interval):
            return False
        if self.is_empty:
            return True
        if other.is_empty:
            return False
        return other.lo <= self.lo and other.hi >= self.hi
    
    def proper_subset(self, other):
        if not isinstance(other, Interval):
            return False
        return self.subset(other) and self != other
    
    def overlaps(self, other):
        if not isinstance(other, Interval):
            return False
        if self.is_empty or other.is_empty:
            return False
        return max(other.lo, self.lo) <= min(self.hi, other.hi)

    def intersection(self, other):
        if not isinstance(other, Interval):
            return Interval(Number('nan'), Number('nan'))
        if self.is_empty or other.is_empty:
            return Interval.empty()
        return Interval(max(self.lo, other.lo), min(self.hi, other.hi))
    
    def hull(self, other):
        if not isinstance(other, Interval):
            return Interval(Number('nan'), Number('nan'))
        if self.is_empty:
            return other
        if other.is_empty:
            return self
        return Interval(min(self.lo, other.lo), max(self.hi, other.hi))

    def __repr__(self):
        if self.is_empty:
            return "Interval.empty()"
        if self.is_entire:
            return "Interval.entire()"
        return f"Interval({self.lo}, {self.hi})"

    def __str__(self):
        if self.is_empty:
            return "[empty]"
        if self.is_entire:
            return "[entire]"
        return f"[{self.lo}, {self.hi}]"

    def disjoint(self, other):
        if not isinstance(other, Interval):
            return False
        return not self.overlaps(other)

    def interior_contains(self, x):
        try:
            x = Number(x)
        except:
            return False
        if self.is_empty:
            return False
        return self.lo < x < self.hi

    def interior(self, other):
        if not isinstance(other, Interval):
            return False
        if self.is_empty:
            return True
        if other.is_empty:
            return False
        if self.is_entire and other.is_entire:
            return True

        return other.lo < self.lo and self.hi < other.hi

    def precedes(self, other):
        other = self._coerce(other)
        if self.is_empty or other.is_empty:
            return True
        return self.hi <= other.lo

    def meets(self, other):
        if not isinstance(other, Interval):
            return False
        if self.is_empty or other.is_empty:
            return False
        return self.hi == other.lo or other.hi == self.lo

    def __add__(self, other):
        from .arithmetic import add
        other = self._coerce(other)
        return add(self, other)

    def __sub__(self, other):
        from .arithmetic import sub
        other = self._coerce(other)
        return sub(self, other)

    def __mul__(self, other):
        from .arithmetic import mul
        other = self._coerce(other)
        return mul(self, other)

    def __truediv__(self, other):
        from .arithmetic import div
        other = self._coerce(other)
        return div(self, other)

    def __neg__(self):
        if self.is_empty:
            return Interval.empty()
        return Interval(-self.hi, -self.lo)

    def __abs__(self):
        if self.is_empty:
            return Interval.empty()

        if self.lo >= 0:
            return self
        if self.hi <= 0:
            return Interval(-self.hi, -self.lo)
        return Interval(Number(0), Number(max(-self.lo, self.hi)))

    def __radd__(self, other):
        from .arithmetic import add
        other = self._coerce(other)
        return add(other, self)

    def __rsub__(self, other):
        from .arithmetic import sub
        other = self._coerce(other)
        return sub(other, self)

    def __rmul__(self, other):
        from .arithmetic import mul
        other = self._coerce(other)
        return mul(other, self)

    def __rtruediv__(self, other):
        from .arithmetic import div
        other = self._coerce(other)
        return div(other, self)
    
    @property
    def is_strictly_positive(self):
        return not self.is_empty and self.lo > 0

    @property
    def is_strictly_negative(self):
        return not self.is_empty and self.hi < 0
    
    @property
    def is_nonnegative(self):
        return not self.is_empty and self.lo >= 0

    @property
    def is_nonpositive(self):
        return not self.is_empty and self.hi <= 0

    @property
    def contains_zero(self):
        return self.contains(0)

    def __eq__(self, other):
        other = self._coerce(other)
        if self.is_empty and other.is_empty:
            return True
        return self.lo == other.lo and self.hi == other.hi
    
    def __lt__(self, other):
        other = self._coerce(other)
        if self.is_empty and other.is_empty:
            return True
        if self.is_empty or other.is_empty:
            return False
        return self.lo <= other.lo and self.hi <= other.hi

    def __gt__(self, other):
        if not isinstance(other, Interval):
            other = self._coerce(other)
        if self.is_empty or other.is_empty:
            return False
        return self.lo >= other.lo and self.hi >= other.hi

    def strictly_less_than(self, other):
        other = self._coerce(other)
        if self.is_empty and other.is_empty:
            return True
        if self.is_entire and other.is_entire:
            return True
        if other.is_empty or self.is_empty:
            return False
        return self.lo < other.lo and self.hi < other.hi

    def bisect(self):
        if self.is_empty:
            return (Interval.empty(), Interval.empty())

        m = self.midpoint
        return (Interval(self.lo, m), Interval(m, self.hi))

    def inf_sub(self, other):
        other = self._coerce(other)
        if self.is_empty or other.is_empty:
            return Number('nan')
        with context(get_context()) as ctx:
            ctx.round = RoundDown
            return self.lo - other.lo

    def sup_sub(self, other):
        other = self._coerce(other)
        if self.is_empty or other.is_empty:
            return Number('nan')
        with context(get_context()) as ctx:
            ctx.round = RoundUp
            return self.hi - other.hi

    def strictly_precedes(self, other):
        other = self._coerce(other)
        if self.is_empty or other.is_empty:
            return True
        return self.hi < other.lo

    def __neg__(self):
        if self.is_empty:
            return self
        if self.is_entire:
            return self
        return Interval(-self.hi, -self.lo)
    
    @property
    def inf(self):
        return self.lo
    
    @property
    def sup(self):
        return self.hi
