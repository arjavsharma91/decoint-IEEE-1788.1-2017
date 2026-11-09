from .interval import Interval
from .arithmetic import add as bare_add, sub as bare_sub, mul as bare_mul, div as bare_div, reciprocal as bare_reciprocal, fma as bare_fma
from .decorations import Decoration, combine
from .decorated_interval import DecoratedInterval

def _finalize_decoration(base_dec: Decoration, interval: Interval) -> Decoration:
  """
  Finalize a decoration based on the boundedness of the resulting interval.

  Parameters
  ----------
  base_dec : Decoration
      The base combined decoration.
  interval : Interval
      The resulting interval.

  Returns
  -------
  Decoration
      The finalized decoration.
  """
  if base_dec == Decoration.COM and not interval.is_bounded:
    return Decoration.DAC
  return base_dec

def add(x: DecoratedInterval, y: DecoratedInterval) -> DecoratedInterval:
  """
  Perform decorated interval addition.

  Parameters
  ----------
  x : DecoratedInterval
      First decorated interval operand.
  y : DecoratedInterval
      Second decorated interval operand.

  Returns
  -------
  DecoratedInterval
      The resulting decorated interval sum.
  """
  x = DecoratedInterval._coerce(x)
  y = DecoratedInterval._coerce(y)

  if x.is_nai or y.is_nai:
    return DecoratedInterval.new_nai()

  interval = bare_add(x.interval, y.interval)
  dec = combine(x.decoration, y.decoration)
  dec = _finalize_decoration(dec, interval)

  return DecoratedInterval(interval, dec)

def sub(x: DecoratedInterval, y: DecoratedInterval) -> DecoratedInterval:
  """
  Perform decorated interval subtraction.

  Parameters
  ----------
  x : DecoratedInterval
      Minuend decorated interval.
  y : DecoratedInterval
      Subtrahend decorated interval.

  Returns
  -------
  DecoratedInterval
      The resulting decorated interval difference.
  """
  x = DecoratedInterval._coerce(x)
  y = DecoratedInterval._coerce(y)

  if x.is_nai or y.is_nai:
    return DecoratedInterval.new_nai()

  interval = bare_sub(x.interval, y.interval)
  dec = combine(x.decoration, y.decoration)
  dec = _finalize_decoration(dec, interval)

  return DecoratedInterval(interval, dec)

def mul(x: DecoratedInterval, y: DecoratedInterval) -> DecoratedInterval:
  """
  Perform decorated interval multiplication.

  Parameters
  ----------
  x : DecoratedInterval
      First decorated interval factor.
  y : DecoratedInterval
      Second decorated interval factor.

  Returns
  -------
  DecoratedInterval
      The resulting decorated interval product.
  """
  x = DecoratedInterval._coerce(x)
  y = DecoratedInterval._coerce(y)

  if x.is_nai or y.is_nai:
    return DecoratedInterval.new_nai()

  interval = bare_mul(x.interval, y.interval)
  dec = combine(x.decoration, y.decoration)
  dec = _finalize_decoration(dec, interval)

  return DecoratedInterval(interval, dec)

def reciprocal(x: DecoratedInterval) -> DecoratedInterval:
  """
  Compute the reciprocal of a decorated interval.

  Parameters
  ----------
  x : DecoratedInterval
      Input decorated interval.

  Returns
  -------
  DecoratedInterval
      The resulting reciprocal decorated interval.
  """
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  if x.interval.contains(0):
    if x.interval.lo < 0 and x.interval.hi > 0:
      return DecoratedInterval(Interval.entire(), Decoration.TRV)
    interval = bare_reciprocal(x.interval)
    return DecoratedInterval(interval, Decoration.TRV)
  interval = bare_reciprocal(x.interval)
  dec = x.decoration
  dec = _finalize_decoration(dec, interval)
  return DecoratedInterval(interval, dec)

def div(x: DecoratedInterval, y: DecoratedInterval) -> DecoratedInterval:
  """
  Perform decorated interval division.

  Parameters
  ----------
  x : DecoratedInterval
      Numerator decorated interval.
  y : DecoratedInterval
      Denominator decorated interval.

  Returns
  -------
  DecoratedInterval
      The resulting decorated interval quotient.
  """
  x = DecoratedInterval._coerce(x)
  y = DecoratedInterval._coerce(y)

  if x.is_nai or y.is_nai:
    return DecoratedInterval.new_nai()

  if x.is_empty or y.is_empty:
    return DecoratedInterval.empty()

  if y.interval.contains(0):
      interval = bare_div(x.interval, y.interval)
      dec = combine(x.decoration, y.decoration, Decoration.TRV)
      return DecoratedInterval(interval, Decoration.TRV)

  interval = bare_div(x.interval, y.interval)
  dec = combine(x.decoration, y.decoration)
  dec = _finalize_decoration(dec, interval)

  return DecoratedInterval(interval, dec)

def fma(x: DecoratedInterval, y: DecoratedInterval, z: DecoratedInterval) -> DecoratedInterval:
  x = DecoratedInterval._coerce(x)
  y = DecoratedInterval._coerce(y)
  z = DecoratedInterval._coerce(z)

  if x.is_nai or y.is_nai or z.is_nai:
    return DecoratedInterval.new_nai()

  interval = bare_fma(x.interval, y.interval, z.interval)
  dec = combine(x.decoration, y.decoration, z.decoration)

  dec = _finalize_decoration(dec, interval)

  return DecoratedInterval(interval, dec)
