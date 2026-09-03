from .decorated_interval import DecoratedInterval
from .decorations import Decoration, combine
from .functions import exp as bare_exp, sqrt as bare_sqrt, log as bare_log, pow_int as bare_pow_int, sign as bare_sign, interval_min as bare_interval_min, interval_max as bare_interval_max, nth_root as bare_nth_root, sin as bare_sin, cos as bare_cos, tan as bare_tan, asin as bare_asin, acos as bare_acos, atan as bare_atan, sinh as bare_sinh, cosh as bare_cosh, tanh as bare_tanh, asinh as bare_asinh, acosh as bare_acosh, atanh as bare_atanh, abs as bare_abs, atan2 as bare_atan2, contains_periodic_point as bare_contains_periodic_point, sqr as bare_sqr, pow_interval as bare_pow_interval, exp2 as bare_exp2, exp10 as bare_exp10, log2 as bare_log2, log10 as bare_log10, interval_ceil as bare_interval_ceil, interval_floor as bare_interval_floor, interval_trunc as bare_interval_trunc
from .constants import PI, HALF_PI, TWO_PI
from .interval import Interval
from gmpy2 import mpfr, is_integer, is_infinite, floor, ceil, trunc

def exp(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  interval = bare_exp(x.interval)
  dec = combine(x.decoration)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC
  return DecoratedInterval(interval, dec)

def sqrt(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  if x.interval.hi < 0:
    return DecoratedInterval.empty()
  elif x.interval.lo < 0:
    op_dec = Decoration.TRV
  else:
    op_dec = Decoration.COM
  interval = bare_sqrt(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def log(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  if x.interval.hi <= 0:
    return DecoratedInterval.empty()
  elif x.interval.lo <= 0:
    op_dec = Decoration.TRV
  else:
    op_dec = Decoration.COM
  interval = bare_log(x.interval)
  dec = combine(x.decoration, op_dec)
  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC
  return DecoratedInterval(interval, dec)

def pow_int(x, n):
  x = DecoratedInterval._coerce(x)
  try:
    n_int = int(n)
    if n_int != n:
      return DecoratedInterval.new_nai()
  except Exception:
    return DecoratedInterval.new_nai()
  if x.is_nai:
    return DecoratedInterval.new_nai()

  if n_int < 0 and x.interval.contains(0):
    op_dec = Decoration.TRV
  else:
    op_dec = Decoration.COM

  interval = bare_pow_int(x.interval, n_int)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC
  return DecoratedInterval(interval, dec)

def sign(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  if x.interval.contains(0) and not x.interval.is_singleton:
    op_dec = Decoration.DEF
  else:
    op_dec = Decoration.COM

  interval = bare_sign(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC
  return DecoratedInterval(interval, dec)

def interval_min(x, y):
  x = DecoratedInterval._coerce(x)
  y = DecoratedInterval._coerce(y)

  if x.is_nai or y.is_nai:
    return DecoratedInterval.new_nai()
  op_dec = Decoration.COM
  interval = bare_interval_min(x.interval, y.interval)

  dec = combine(op_dec, y.decoration, x.decoration)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC
  return DecoratedInterval(interval, dec)

def interval_max(x, y):
  x = DecoratedInterval._coerce(x)
  y = DecoratedInterval._coerce(y)

  if x.is_nai or y.is_nai:
    return DecoratedInterval.new_nai()
  op_dec = Decoration.COM
  interval = bare_interval_max(x.interval, y.interval)

  dec = combine(op_dec, y.decoration, x.decoration)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC
  return DecoratedInterval(interval, dec)

def nth_root(x, n):
  x = DecoratedInterval._coerce(x)
  try:
    n_int = int(n)
    if n_int != n:
      return DecoratedInterval.new_nai()
  except Exception:
    return DecoratedInterval.new_nai()
  if x.is_nai:
    return DecoratedInterval.new_nai()
  if n_int <= 0:
    return DecoratedInterval.new_nai()
  if n_int % 2 == 1:
    op_dec = Decoration.COM
  else:
    if x.interval.hi < 0:
      return DecoratedInterval.empty()
    elif x.interval.lo < 0:
      op_dec = Decoration.TRV
    else:
      op_dec = Decoration.COM
  interval = bare_nth_root(x.interval, n_int)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def sin(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  op_dec = Decoration.COM

  interval = bare_sin(x.interval)
  dec = combine(op_dec, x.decoration)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)


def cos(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  op_dec = Decoration.COM

  interval = bare_cos(x.interval)
  dec = combine(op_dec, x.decoration)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def tan(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  if x.interval.is_empty:
    return DecoratedInterval.empty()
  if not x.interval.is_bounded:
    return DecoratedInterval(Interval.entire(), Decoration.TRV)

  if bare_contains_periodic_point(x.interval, HALF_PI, PI):
    op_dec = Decoration.TRV
  else:
    op_dec = Decoration.COM

  interval = bare_tan(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def asin(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()

  if x.interval.hi < -1 or x.interval.lo > 1:
    return DecoratedInterval.empty()
  elif x.interval.lo < -1 or x.interval.hi > 1:
    op_dec = Decoration.TRV
  else:
    op_dec = Decoration.COM

  interval = bare_asin(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def acos(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()

  if x.interval.hi < -1 or x.interval.lo > 1:
    return DecoratedInterval.empty()
  elif x.interval.lo < -1 or x.interval.hi > 1:
    op_dec = Decoration.TRV
  else:
    op_dec = Decoration.COM

  interval = bare_acos(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def atan(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  op_dec = Decoration.COM

  interval = bare_atan(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def sinh(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  op_dec = Decoration.COM

  interval = bare_sinh(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def cosh(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  op_dec = Decoration.COM

  interval = bare_cosh(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def tanh(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  op_dec = Decoration.COM

  interval = bare_tanh(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)
  
def asinh(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  op_dec = Decoration.COM

  interval = bare_asinh(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def acosh(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  if x.interval.hi < 1:
    return DecoratedInterval.empty()
  elif x.interval.lo < 1:
    op_dec = Decoration.TRV
  else:
    op_dec = Decoration.COM

  interval = bare_acosh(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def atanh(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()

  if x.interval.hi <= -1 or x.interval.lo >= 1:
    return DecoratedInterval.empty()
  elif x.interval.lo <= -1 or x.interval.hi >= 1:
    op_dec = Decoration.TRV
  else:
    op_dec = Decoration.COM

  interval = bare_atanh(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)


def abs(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  op_dec = Decoration.COM

  interval = bare_abs(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def atan2(y, x):
  y = DecoratedInterval._coerce(y)
  x = DecoratedInterval._coerce(x)

  if y.is_nai or x.is_nai:
    return DecoratedInterval.new_nai()

  if y.interval.contains(0) and x.interval.contains(0):
    if y.interval.lo == 0 and y.interval.hi == 0 and x.interval.lo == 0 and x.interval.hi == 0:
      return DecoratedInterval.empty()
    op_dec = Decoration.TRV
  elif x.interval.lo < 0 and y.interval.contains(0):
    op_dec = Decoration.DEF if y.interval.lo < 0 else Decoration.DAC
  else:
    op_dec = Decoration.COM

  interval = bare_atan2(y.interval, x.interval)
  dec = combine(x.decoration, op_dec, y.decoration)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def sqr(x):
  x = DecoratedInterval._coerce(x)

  if x.is_nai:
    return DecoratedInterval.new_nai()

  op_dec = Decoration.COM
    
  interval = bare_sqr(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC
  return DecoratedInterval(interval, dec)

def pow_interval(x, y):
  x = DecoratedInterval._coerce(x)
  y = DecoratedInterval._coerce(y)

  if x.is_nai or y.is_nai:
    return DecoratedInterval.new_nai()

  interval = bare_pow_interval(x.interval, y.interval)

  if interval.is_empty:
    return DecoratedInterval(interval, Decoration.TRV)

  dec = combine(x.decoration, y.decoration)

  if x.interval.lo < 0 or (x.interval.lo <= 0 <= x.interval.hi and y.interval.lo <= 0):
    dec = Decoration.TRV
  elif dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def exp2(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  interval = bare_exp2(x.interval)
  dec = combine(x.decoration)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC
  return DecoratedInterval(interval, dec)

def exp10(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  interval = bare_exp10(x.interval)
  dec = combine(x.decoration)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC
  return DecoratedInterval(interval, dec)

def log2(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  if x.interval.hi <= 0:
    return DecoratedInterval.empty()
  elif x.interval.lo <= 0:
    op_dec = Decoration.TRV
  else:
    op_dec = Decoration.COM
  interval = bare_log2(x.interval)
  dec = combine(x.decoration, op_dec)
  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC
  return DecoratedInterval(interval, dec)

def log10(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  if x.interval.hi <= 0:
    return DecoratedInterval.empty()
  elif x.interval.lo <= 0:
    op_dec = Decoration.TRV
  else:
    op_dec = Decoration.COM
  interval = bare_log10(x.interval)
  dec = combine(x.decoration, op_dec)
  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC
  return DecoratedInterval(interval, dec)

def interval_ceil(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  
  res_interval = bare_interval_ceil(x.interval)
    
  if not x.interval.is_bounded:
    has_jump = True
    contains_integer = True
  else:
    has_jump = (x.interval.lo < x.interval.hi and ceil(x.interval.lo) < x.interval.hi)
    contains_integer = floor(x.interval.hi) >= ceil(x.interval.lo)
  
  if has_jump:
    dec = min(x.decoration, Decoration.DEF)
  elif contains_integer:
    dec = min(x.decoration, Decoration.DAC)
  else:
    dec = x.decoration

  return DecoratedInterval(res_interval, dec)

def interval_floor(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  
  res_interval = bare_interval_floor(x.interval)
  
  x_low = mpfr(x.interval.lo)
  x_high = mpfr(x.interval.hi)

  if x.interval.is_bounded:
    has_jump = x_low < x_high and x_low < floor(x_high)
    contains_integer = floor(x_high) >= ceil(x_low)
  else:
    has_jump = True
  
  if has_jump:
    dec = min(x.decoration, Decoration.DEF)
  elif contains_integer:
    dec = min(x.decoration, Decoration.DAC)
  else:
    dec = x.decoration

  return DecoratedInterval(res_interval, dec)

def interval_trunc(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  
  res_interval = bare_interval_trunc(x.interval)
  
  x_low = x.interval.lo
  x_high = x.interval.hi

  if not x.interval.is_bounded:
    has_jump = True
    contains_integer = True
  else:
    
    has_jump = False
    if x_low < x_high:
      if x_low < 0:
        bound_high = min(x_high, mpfr(0))
        if ceil(x_low) < bound_high:
          has_jump = True
      if x_high > 0 and not has_jump:
        bound_low = max(x_low, mpfr(0))
        if bound_low < floor(x_high):
          has_jump = True

    contains_nonzero_integer = (
      (floor(x_high) >= ceil(x_low)) and 
      not (floor(x_low) == -1 and floor(x_high) == 0)
    ) or (is_integer(x_low) and x_low != 0) or (is_integer(x_high) and x_high != 0)
  
  if has_jump:
    dec = min(x.decoration, Decoration.DEF)
  elif contains_nonzero_integer:
    dec = min(x.decoration, Decoration.DAC)
  else:
    dec = x.decoration

  return DecoratedInterval(res_interval, dec)
