import random
from gmpy2 import mpfr
from intervals.interval import Interval

def rand_number(low=-10, high=10):
  return mpfr(random.uniform(low, high))

def rand_interval():
  a = rand_number()
  b = rand_number()
  return Interval(min(a, b), max(a, b))

def empty_interval():
  return Interval.empty()

def entire_interval():
  return Interval.entire()

def zero_crossing_interval():
  return Interval(-1, 1)

def point_interval():
  x = rand_number()
  return Interval(x, x)

def rand_interval_mixed():
  r = random.random()

  if r < 0.2:
    return empty_interval()
  elif r < 0.4:
    return entire_interval()
  elif r < 0.6:
    return zero_crossing_interval()
  elif r < 0.8:
    return point_interval()
  else:
    return rand_interval()

def sample(x: Interval):
  if x.is_empty:
    raise ValueError("Cannot sample empty interval")

  if x.lo == x.hi:
    return x.lo

  return mpfr(random.uniform(float(x.lo), float(x.hi)))

def assert_contains(x: Interval, value):
  assert x.lo <= value <= x.hi, f"Value {value} not in interval {x}"

def run_property_test(trials, test_fn):
  for _ in range(trials):
    test_fn()
