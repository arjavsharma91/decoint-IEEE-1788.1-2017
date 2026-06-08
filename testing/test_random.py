from intervals.arithmetic import add, sub, mul, div
from intervals.interval import Interval
from tests.utils import rand_interval_mixed, sample, assert_contains

def test_add_containment():
  x = rand_interval_mixed()
  y = rand_interval_mixed()

  a = sample(x)
  b = sample(y)

  result = add(x, y)

  assert_contains(result, a + b)

def test_sub_containment():
  x = rand_interval_mixed()
  y = rand_interval_mixed()

  a = sample(x)
  b = sample(y)

  result = sub(x, y)

  assert_contains(result, a - b)

def test_mul_containment():
  x = rand_interval_mixed()
  y = rand_interval_mixed()

  a = sample(x)
  b = sample(y)

  result = mul(x, y)

  assert_contains(result, a * b)

from intervals.arithmetic import reciprocal

def test_reciprocal():
  x = rand_interval_mixed()

  if x.contains(0):
    return

  a = sample(x)

  result = reciprocal(x)

  assert_contains(result, 1 / a)

def test_div_containment():
  x = rand_interval_mixed()
  y = rand_interval_mixed()

  if y.is_empty:
        return

  result = div(x, y)

  if y.contains(0):
    assert result.is_entire or result == Interval.entire()
    return
  a = sample(x)
  b = sample(y)

  if b == 0:
    return

  assert_contains(result, a / b)
