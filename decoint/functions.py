from .interval import Interval
from .rounding import add_up, add_down, sub_up, sub_down, mul_up, mul_down, div_up, div_down, sqrt_up, sqrt_down, exp_down, exp_up, log_up, log_down, pow_up, pow_down, root_up, root_down, sin_up, sin_down, tan_up, tan_down, asin_up, asin_down, acos_up, acos_down, atan_up, atan_down, sinh_up, sinh_down, cosh_up, cosh_down, tanh_up, tanh_down, atanh_up, atanh_down, asinh_up, asinh_down, acosh_up, acosh_down, cos_up, cos_down, sqr_up, sqr_down, pow_down_interval, pow_up_interval, exp2_up, exp2_down, log2_up, log2_down, exp10_up, exp10_down, log10_up, log10_down, atan2_down, atan2_up
from gmpy2 import mpfr, floor, ceil, context, get_context, is_zero, RoundDown, RoundUp, trunc
from .arithmetic import reciprocal
from .constants import PI, TWO_PI, HALF_PI
import builtins

Number = mpfr
ctx = get_context()
ctx.precision = 53
ctx.emin = -1073
ctx.emax = 1024

ZERO = mpfr(0)
with context(get_context(), round = RoundDown):
  PI_DN = Number(PI)
  HALF_PI_DN = Number(HALF_PI)
  TWO_PI_DN = Number(TWO_PI)
with context(get_context(), round = RoundUp):
  PI_UP = Number(PI)
  HALF_PI_UP = Number(HALF_PI)
  TWO_PI_UP = Number(TWO_PI)

MPI_DN = -PI_UP
MPI_UP = -PI_DN
MHALF_PI_DN = -HALF_PI_UP
MHALF_PI_UP = -HALF_PI_DN

def sqrt(x: Interval) -> Interval:
  x = Interval._coerce(x)
  if x.is_empty:
    return Interval.empty()
  if x.hi < 0:
    return Interval.empty()
  lo = max(x.lo, mpfr(0))
  return Interval(sqrt_down(lo), sqrt_up(x.hi))

def exp(x) -> Interval:
  x = Interval._coerce(x)
  if x.is_empty:
    return Interval.empty()
  return Interval(exp_down(x.lo), exp_up(x.hi))

def log(x) -> Interval:
  x = Interval._coerce(x)
  if x.is_empty:
    return Interval.empty()
  if x.hi <= 0:
    return Interval.empty()
  if x.lo <= 0:
    lo = mpfr('-inf')
  else:
    lo = log_down(x.lo)
  hi = log_up(x.hi)
  return Interval(lo, hi)

def pow_int(x, n):
  x = Interval._coerce(x)
  if x.is_empty:
    return Interval.empty()
  try:
    n_int = int(n)
    if n_int != n:
      return Interval(mpfr('nan'), mpfr('nan'))
  except Exception:
    return Interval(mpfr('nan'), mpfr('nan'))
  if n_int == 0:
    return Interval(mpfr(1), mpfr(1))
  if n_int < 0:
    return reciprocal(pow_int(x, -n_int))
  if n_int % 2 == 1:
    lo = pow_down(x.lo, n_int)
    hi = pow_up(x.hi, n_int)
    return Interval(lo, hi)
  if n_int % 2 == 0:
    if x.lo >= 0:
      lo = pow_down(x.lo, n_int)
      hi = pow_up(x.hi, n_int)
      return Interval(lo, hi)
    if x.hi <= 0:
      hi_sub = builtins.abs(x.hi)
      lo_sub = builtins.abs(x.lo)
      lo = pow_down(hi_sub, n_int)
      hi = pow_up(lo_sub, n_int)
      return Interval(lo, hi)
    hi_sub = builtins.abs(x.hi)
    lo_sub = builtins.abs(x.lo)
    hi = max(
    pow_up(hi_sub, n_int),
    pow_up(lo_sub, n_int)
    )
    return Interval(mpfr(0), hi)

def sign(x) -> Interval:
  x = Interval._coerce(x)
  if x.is_empty:
    return Interval.empty()
  if x.lo > 0:
    return Interval(Number(1), Number(1))
  if x.hi < 0:
    return Interval(Number(-1), Number(-1))
  if x.lo == 0 and x.hi == 0:
    return Interval(Number(0), Number(0))
  if x.lo == 0:
    return Interval(Number(0), Number(1))
  if x.hi == 0:
    return Interval(Number(-1), Number(0))
  return Interval(Number(-1), Number(1))

def interval_min(x, y) -> Interval:
  x = Interval._coerce(x)
  y = Interval._coerce(y)
  if x.is_empty or y.is_empty:
    return Interval.empty()
  return Interval(min(x.lo, y.lo), min(x.hi, y.hi))

def interval_max(x, y) -> Interval:
  x = Interval._coerce(x)
  y = Interval._coerce(y)
  
  if x.is_empty or y.is_empty:
    return Interval.empty()
  return Interval(max(x.lo, y.lo), max(x.hi, y.hi))
  
def nth_root(x, n) -> Interval:
  x = Interval._coerce(x)
  try:
    n_int = int(n)
    if n_int != n:
      return Interval(mpfr('nan'), mpfr('nan'))
  except Exception:
    return Interval(mpfr('nan'), mpfr('nan'))
  if n_int <= 0:
    return Interval(mpfr('nan'), mpfr('nan'))
  if x.is_empty:
    return Interval.empty()
  if n_int % 2 == 1:
    return Interval(root_down(x.lo, n), root_up(x.hi, n))
  if x.hi < 0:
    return Interval.empty()
  lo = max(x.lo, mpfr(0))
  return Interval(root_down(lo, n_int), root_up(x.hi, n_int))

def contains_periodic_point(x, offset, period, prec = 128):
  with context(get_context(), precision = prec):
    off_val = offset() if callable(offset) else offset
    per_val = period() if callable(offset) else period

    lo_mpfr = mpfr(str(x.lo))
    hi_mpfr = mpfr(str(x.hi))
    off_mpfr = mpfr(str(off_val))
    per_mpfr = mpfr(str(per_val))

    if hi_mpfr - lo_mpfr >= per_mpfr:
      return True

    k_lo = (lo_mpfr - off_mpfr) / per_mpfr
    k_hi = (hi_mpfr - off_mpfr) / per_mpfr

    return ceil(k_lo) <= floor(k_hi)
def sin(x) -> Interval:
  x = Interval._coerce(x)
  if x.is_empty:
    return Interval.empty()
  if x.width >= TWO_PI:
    return Interval(mpfr(-1), mpfr(1))
  s1 = sin_down(x.lo)
  s2 = sin_down(x.hi)
  t1 = sin_up(x.lo)
  t2 = sin_up(x.hi)
  lo = min(s1, s2)
  hi = max(t1, t2)

  if contains_periodic_point(x, HALF_PI, TWO_PI):
    hi = mpfr(1)
  if contains_periodic_point(x, -HALF_PI, TWO_PI):
    lo = mpfr(-1)
  return Interval(lo, hi)

def cos(x) -> Interval:
  x = Interval._coerce(x)
  if x.is_empty:
    return Interval.empty()
  if x.width >= TWO_PI:
    return Interval(mpfr(-1), mpfr(1))
        
  c1 = cos_down(x.lo)
  c2 = cos_down(x.hi)
  d1 = cos_up(x.lo)
  d2 = cos_up(x.hi)
  lo = min(c1, c2)
  hi = max(d1, d2)

    # Cosine peaks at 0 (mod 2pi), troughs at pi (mod 2pi)
  if contains_periodic_point(x, mpfr(0), TWO_PI):
    hi = mpfr(1)
  if contains_periodic_point(x, PI, TWO_PI):
    lo = mpfr(-1)
  return Interval(lo, hi)
  
def tan(x):
  x = Interval._coerce(x)
  if x.is_empty:
    return Interval.empty()
  if x.width >= PI:
    return Interval.entire()
  if contains_periodic_point(x, HALF_PI, PI):
    return Interval.entire()
  lo = tan_down(x.lo)
  hi = tan_up(x.hi)
  return Interval(lo, hi)

def asin(x):
  x = Interval._coerce(x)
  if x.is_empty:
    return Interval.empty()
  x = x.intersection(Interval(-1, 1))

  if x.is_empty:
    return Interval.empty()
  return Interval(asin_down(x.lo), asin_up(x.hi))

def acos(x):
  x = Interval._coerce(x)
  if x.is_empty:
    return Interval.empty()
  x = x.intersection(Interval(-1, 1))
  if x.is_empty:
    return Interval.empty()
  return Interval(acos_down(x.hi), acos_up(x.lo))

def atan(x):
  x = Interval._coerce(x)

  if x.is_empty:
    return Interval.empty()

  return Interval(
    atan_down(x.lo),
    atan_up(x.hi)
    )

def sinh(x):
  x = Interval._coerce(x)
  if x.is_empty:
    return Interval.empty()
  return Interval(sinh_down(x.lo), sinh_up(x.hi))

def tanh(x):
  x = Interval._coerce(x)
  if x.is_empty:
    return Interval.empty()
  return Interval(tanh_down(x.lo), tanh_up(x.hi))

def cosh(x):
  x = Interval._coerce(x)
  if x.is_empty:
    return Interval.empty()

  if x.lo >= 0:
    return Interval(cosh_down(x.lo), cosh_up(x.hi))
  if x.hi <= 0:
    return Interval(cosh_down(x.hi), cosh_up(x.lo))
  return Interval(mpfr(1), max(cosh_up(x.lo), cosh_up(x.hi)))

def asinh(x) -> Interval:
  x = Interval._coerce(x)
  if x.is_empty:
    return Interval.empty()
  return Interval(asinh_down(x.lo), asinh_up(x.hi))

def acosh(x) -> Interval:
  x = Interval._coerce(x)
  if x.is_empty:
    return Interval.empty()
  if x.hi < 1:
    return Interval.empty()
        

  lo = max(x.lo, mpfr(1))
  return Interval(acosh_down(lo), acosh_up(x.hi))

def atanh(x) -> Interval:
  x = Interval._coerce(x)
  if x.is_empty:
    return Interval.empty()
    
  x = x.intersection(Interval(-1, 1))
  if x.is_empty:
    return Interval.empty()
        
  lo = mpfr('-inf') if x.lo <= -1 else atanh_down(x.lo)
  hi = mpfr('inf') if x.hi >= 1 else atanh_up(x.hi)
    
  return Interval(lo, hi)

def abs(x):
  x = Interval._coerce(x)
  if x.is_empty:
    return Interval.empty()
  if x.lo >= 0:
    return Interval(x.lo, x.hi)
  elif x.hi <= 0:
    return Interval(-x.hi, -x.lo)

  hi = max(-x.lo, x.hi)
  return Interval(Number(0), hi)

def safe_atan2_dn(y, x):
  y_val = ZERO if is_zero(y) else y
  x_val = ZERO if is_zero(x) else x
  return atan2_down(y_val, x_val)

def safe_atan2_up(y, x):
  y_val = ZERO if is_zero(y) else y
  x_val = ZERO if is_zero(x) else x
  return atan2_up(y_val, x_val)

def atan2(y, x):
  y = Interval._coerce(y)
  x = Interval._coerce(x)

  # 1. Empty set handling
  if y.is_empty or x.is_empty:
    return Interval.empty()

  # 2. Undefined origin point (0, 0) handling
  if y.lo == ZERO and y.hi == ZERO and x.lo == ZERO and x.hi == ZERO:
    return Interval.empty()

  y1, y2 = y.lo, y.hi
  x1, x2 = x.lo, x.hi

  # Case 1: X is strictly positive (x1 > 0)
  if x1 > ZERO:
    if y1 >= ZERO:
      lo = safe_atan2_dn(y1, x2)
      hi = safe_atan2_up(y2, x1)
    elif y2 <= ZERO:
      lo = safe_atan2_dn(y1, x1)
      hi = safe_atan2_up(y2, x2)
    else:
      lo = safe_atan2_dn(y1, x1)
      hi = safe_atan2_up(y2, x1)

  # Case 2: X is strictly negative (x2 < 0)
  elif x2 < ZERO:
    if y1 > ZERO:
      lo = safe_atan2_dn(y2, x2)
      hi = safe_atan2_up(y1, x1)
    elif y2 < ZERO:
      lo = safe_atan2_dn(y2, x1)
      hi = safe_atan2_up(y1, x2)
    elif y1 == ZERO and y2 == ZERO:
      lo, hi = PI_DN, PI_UP
    elif y1 == ZERO and y2 > ZERO:
      lo = safe_atan2_dn(y2, x2)
      hi = PI_UP
    else:  # y1 < ZERO and y2 >= ZERO
      lo, hi = MPI_DN, PI_UP

  # Case 3: X contains zero (x1 <= 0 <= x2)
  else:
    # Subcase 3.0: X is degenerate [0, 0]
    if x1 == ZERO and x2 == ZERO:
      if y1 >= ZERO:
        lo, hi = HALF_PI_DN, HALF_PI_UP
      elif y2 <= ZERO:
        lo, hi = MHALF_PI_DN, MHALF_PI_UP
      else:  # y1 < ZERO and y2 > ZERO
        lo, hi = MHALF_PI_DN, HALF_PI_UP

    # Subcase 3.1: Y is strictly positive
    elif y1 > ZERO:
      lo = safe_atan2_dn(y1, x2)
      hi = safe_atan2_up(y1, x1)

    # Subcase 3.2: Y is strictly negative
    elif y2 < ZERO:
      lo = safe_atan2_dn(y2, x1)
      hi = safe_atan2_up(y2, x2)

    # Subcase 3.3: Y contains zero (y1 <= 0 <= y2) and X is non-degenerate
    else:
      if x1 < ZERO:
        if y1 < ZERO and y2 > ZERO:
          lo, hi = MPI_DN, PI_UP
        elif y1 == ZERO and y2 == ZERO:
          if x2 > ZERO:
            lo, hi = ZERO, PI_UP
          else:  # x2 == ZERO
            lo, hi = PI_DN, PI_UP
        elif y1 == ZERO and y2 > ZERO:
          if x2 > ZERO:
            lo, hi = ZERO, PI_UP
          else:  # x2 == ZERO
            lo, hi = HALF_PI_DN, PI_UP
        else:  # y1 < ZERO and y2 == ZERO
          lo, hi = MPI_DN, PI_UP
      else:  # x1 == ZERO and x2 > ZERO
        if y1 < ZERO and y2 > ZERO:
          lo, hi = MHALF_PI_DN, HALF_PI_UP
        elif y1 == ZERO and y2 == ZERO:
          lo, hi = ZERO, ZERO
        elif y1 == ZERO and y2 > ZERO:
          lo, hi = ZERO, HALF_PI_UP
        else:  # y1 < ZERO and y2 == ZERO
          lo, hi = MHALF_PI_DN, ZERO

  return Interval(lo, hi)
            


def sqr(x):
  x = Interval._coerce(x)
  if x.is_empty:
    return Interval.empty()
  if x.lo >= 0:
    lo = sqr_down(x.lo)
    hi = sqr_up(x.hi)
    return Interval(lo, hi)
  elif x.hi <= 0:
    lo = sqr_down(builtins.abs(x.hi))
    hi = sqr_up(builtins.abs(x.lo))
    return Interval(lo, hi)
  hi = max(sqr_up(builtins.abs(x.hi)), sqr_up(builtins.abs(x.lo)))
  return Interval(mpfr(0), hi)

def pow_interval(x, y):
  x = Interval._coerce(x)
  y = Interval._coerce(y)

  if x.is_empty or y.is_empty:
    return Interval.empty()

  x_lo = max(0, x.lo)
  x_hi = x.hi

  if x_lo > x_hi:
    return Interval.empty()
    
  if x_hi == 0:
    if y.hi <= 0:
      return Interval.empty()
    return Interval(mpfr(0), mpfr(0))

  if x_lo == 0:
    v_down = [
      pow_down_interval(x_hi, y.lo),
      pow_down_interval(x_hi, y.hi)
    ]
    v_up = [
      pow_up_interval(x_hi, y.lo),
      pow_up_interval(x_hi, y.hi)
    ]

    if y.lo > 0 or y.hi > 0:
      v_down.append(mpfr(0))
      v_up.append(mpfr(0))

    if y.lo < 0 or y.hi < 0:
      v_down.append(mpfr('inf'))
      v_up.append(mpfr('inf'))

    if y.lo <= 0 <= y.hi:
      v_down.append(mpfr(1))
      v_up.append(mpfr(1))

  else:
    v_down = [
      pow_down_interval(x_lo, y.lo),
      pow_down_interval(x_lo, y.hi),
      pow_down_interval(x_hi, y.lo),
      pow_down_interval(x_hi, y.hi)
    ]
    v_up = [
      pow_up_interval(x_lo, y.lo),
      pow_up_interval(x_lo, y.hi),
      pow_up_interval(x_hi, y.lo),
      pow_up_interval(x_hi, y.hi)
    ]

  return Interval(min(v_down), max(v_up))

def exp2(x):
  x = Interval._coerce(x)
  
  if x.is_empty:
    return Interval.empty()

  return Interval(exp2_down(x.lo), exp2_up(x.hi))

def exp10(x):
  x = Interval._coerce(x)
  
  if x.is_empty:
    return Interval.empty()

  return Interval(exp10_down(x.lo), exp10_up(x.hi))

def log2(x):
  x = Interval._coerce(x)
  if x.is_empty:
    return Interval.empty()
  if x.hi <= 0:
    return Interval.empty()
  if x.lo <= 0:
    lo = mpfr('-inf')
  else:
    lo = log2_down(x.lo)
  hi = log2_up(x.hi)
  return Interval(lo, hi)

def log10(x):
  x = Interval._coerce(x)
  if x.is_empty:
    return Interval.empty()
  if x.hi <= 0:
    return Interval.empty()
  if x.lo <= 0:
    lo = mpfr('-inf')
  else:
    lo = log10_down(x.lo)
  hi = log10_up(x.hi)
  return Interval(lo, hi)

def interval_ceil(x):
  if x.is_empty:
    return Interval.empty()
  if x.lo == mpfr('-inf'):
    lo = mpfr('-inf')
  else:
    lo = ceil(x.lo)
  if x.hi == mpfr('inf'):
    hi = mpfr('inf')
  else:
    hi = ceil(x.hi)
  return Interval(lo, hi)

def interval_floor(x):
  if x.is_empty:
    return Interval.empty()
  if x.lo == mpfr('-inf'):
    lo = mpfr('-inf')
  else:
    lo = floor(x.lo)
  if x.hi == mpfr('inf'):
    hi = mpfr('inf')
  else:
    hi = floor(x.hi)
  return Interval(lo, hi)

def interval_trunc(x):
  if x.is_empty:
    return Interval.empty()
  if x.lo == mpfr('-inf'):
    lo = mpfr('-inf')
  else:
    lo = trunc(x.lo)
  if x.hi == mpfr('inf'):
    hi = mpfr('inf')
  else:
    hi = trunc(x.hi)
  return Interval(lo, hi)
