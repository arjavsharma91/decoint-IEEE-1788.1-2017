from .interval import Interval
from .rounding import add_down, add_up, sub_down, sub_up, div_down, div_up, mul_down, mul_up, fma_up, fma_down
from gmpy2 import mpfr, is_infinite, is_signed, sign, context, get_context
#Circular Dependency if not careful

ctx = get_context()
ctx.precision = 53
ctx.emin = -1073
ctx.emax = 1024

def add(x, y) -> Interval:
  x = Interval._coerce(x)
  y = Interval._coerce(y)
  if x.is_empty or y.is_empty:
    return Interval.empty()
  lo = add_down(x.lo, y.lo)
  hi = add_up(x.hi, y.hi)
  return Interval(lo, hi)

def sub(x, y) -> Interval:
  x = Interval._coerce(x)
  y = Interval._coerce(y)
  if x.is_empty or y.is_empty:
    return Interval.empty()
  lo = sub_down(x.lo, y.hi)
  hi = sub_up(x.hi, y.lo)
  return Interval(lo, hi)

def mul(x, y) -> Interval:
  x = Interval._coerce(x)
  y = Interval._coerce(y)
  if x.is_empty or y.is_empty:
    return Interval.empty()

  def safe_mul_down(a, b):
    if (a == 0 and is_infinite(b)) or (b == 0 and is_infinite(a)):
      is_neg = is_signed(a) * is_signed(b)
      return mpfr('0') if is_neg else mpfr('-0.0')
    return mul_down(a, b)

  def safe_mul_up(a, b):
    if (a == 0 and is_infinite(b)) or (b == 0 and is_infinite(a)):
      is_neg = is_signed(a) * is_signed(b)
      return mpfr('0') if is_neg else mpfr('-0.0')
    return mul_up(a, b)

  p1 = safe_mul_down(x.lo, y.lo)
  p2 = safe_mul_down(x.lo, y.hi)
  p3 = safe_mul_down(x.hi, y.lo)
  p4 = safe_mul_down(x.hi, y.hi)
  
  lo = min(p1, p2, p3, p4)

  q1 = safe_mul_up(x.lo, y.lo)
  q2 = safe_mul_up(x.lo, y.hi)
  q3 = safe_mul_up(x.hi, y.lo)
  q4 = safe_mul_up(x.hi, y.hi)
  
  hi = max(q1, q2, q3, q4)

  return Interval(lo, hi)

def reciprocal(x) -> Interval:
  x = Interval._coerce(x)
  if x.is_empty:
    return Interval.empty()
  if x.contains_zero:
    if x.lo == 0 and x.hi == 0:
      return Interval.empty()
    if x.lo == 0:
      return Interval(div_down(mpfr(1), x.hi), mpfr('inf'))
    if x.hi == 0:
      return Interval(mpfr('-inf'), div_up(mpfr(1), x.lo))
    return Interval.entire()

  return Interval(div_down(mpfr(1), x.hi), div_up(mpfr(1), x.lo))

def div(x, y) -> Interval:
  x = Interval._coerce(x)
  y = Interval._coerce(y)
  if x.is_empty or y.is_empty:
    return Interval.empty()

  if x.is_entire and not y.contains(0):
    return Interval.entire()

  if y.contains(0):
    if y.hi == 0 and y.lo == 0:
      return Interval.empty()
    if x.hi == 0 and x.lo == 0:
      return Interval(mpfr('0'), mpfr('0'))
    if x.lo >= 0:
      if y.lo == 0:
        return Interval(div_down(x.lo, y.hi), mpfr('inf'))
      elif y.hi == 0:
        return Interval(mpfr('-inf'), div_up(x.lo, y.lo))
      else:
        return Interval.entire()        
    elif x.hi <= 0:
      if y.lo == 0:
        return Interval(mpfr('-inf'), div_up(x.hi, y.hi))
      elif y.hi == 0:
        return Interval(div_down(x.hi, y.lo), mpfr('inf'))
      else:
        return Interval.entire()
    else:
      return Interval.entire()

  # --- CLEAN DIRECT REPLACEMENT FOR mul(x, reciprocal(y)) ---
  if y.lo > 0:  # Denominator is strictly positive
    # Lower bound logic
    if x.lo == mpfr('-inf'):
      lo = mpfr('-inf')
    else:
      lo = div_down(x.lo, y.hi if x.lo >= 0 else y.lo)
    
    # Upper bound logic
    if x.hi == mpfr('inf'):
      hi = mpfr('inf')
    else:
      hi = div_up(x.hi, y.lo if x.hi >= 0 else y.hi)
      
  else:  # Denominator is strictly negative (y.hi < 0)
    # Lower bound logic
    if x.hi == mpfr('inf'):
      lo = mpfr('-inf')
    else:
      lo = div_down(x.hi, y.hi if x.hi >= 0 else y.lo)
      
    # Upper bound logic
    if x.lo == mpfr('-inf'):
      hi = mpfr('inf')
    else:
      hi = div_up(x.lo, y.lo if x.lo >= 0 else y.hi)

  return Interval(lo, hi)

def evaluate_fma_corner(x, y, z, round_up=False):
  # 1. Handle 0 * inf indeterminate form -> results in 0, so 0 + z = z
  if (x == 0 and is_infinite(y)) or (is_infinite(x) and y == 0):
    return z

  # 2. Handle true inf - inf indeterminate form
  if is_infinite(x) or is_infinite(y):
    if is_infinite(z):
      prod_neg = (x < 0) != (y < 0)
      z_neg = z < 0
      # If the infinite product's sign opposes z's infinite sign, it's inf - inf
      if prod_neg != z_neg:
        return None  # Signal containment explosion

  # Safe to compute standard hardware rounded FMA
  return fma_up(x, y, z) if round_up else fma_down(x, y, z)


def fma(x, y, z):
  x = Interval._coerce(x)
  y = Interval._coerce(y)
  z = Interval._coerce(z)

  if x.is_empty or y.is_empty or z.is_empty:
    return Interval.empty()

  # Evaluate lower bound corner combinations
  v_down = []
  for cx in (x.lo, x.hi):
    for cy in (y.lo, y.hi):
      val = evaluate_fma_corner(cx, cy, z.lo, round_up=False)
      if val is None:
        return Interval.entire()
      v_down.append(val)

  # Evaluate upper bound corner combinations
  v_up = []
  for cx in (x.lo, x.hi):
    for cy in (y.lo, y.hi):
      val = evaluate_fma_corner(cx, cy, z.hi, round_up=True)
      if val is None:
        return Interval.entire()
      v_up.append(val)

  return Interval(min(v_down), max(v_up))
