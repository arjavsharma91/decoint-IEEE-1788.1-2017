from gmpy2 import RoundDown, RoundUp, context, get_context, exp, log, mpfr, sin, cos, asin, atan, acos, tan, sqrt, sinh, tanh, cosh, asinh, acosh, atanh, atan2, root, square, fma, exp2, exp10, log2, log10
Number = mpfr
ctx = get_context()
ctx.precision = 53
ctx.emin = -1073
ctx.emax = 1024

def add_down(a: Number, b: Number) -> Number:
    """
    Add two numbers with downward directed rounding.

    Parameters
    ----------
    a : Number
        First operand.
    b : Number
        Second operand.

    Returns
    -------
    Number
        Sum rounded toward negative infinity.
    """
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        mpfr_b = Number(b)
        return mpfr_a + mpfr_b

def add_up(a: Number, b: Number) -> Number:
    """
    Add two numbers with upward directed rounding.

    Parameters
    ----------
    a : Number
        First operand.
    b : Number
        Second operand.

    Returns
    -------
    Number
        Sum rounded toward positive infinity.
    """
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        mpfr_b = Number(b)
        return mpfr_a + mpfr_b

def sub_down(a: Number, b: Number) -> Number:
    """
    Subtract two numbers with downward directed rounding.

    Parameters
    ----------
    a : Number
        Minuend.
    b : Number
        Subtrahend.

    Returns
    -------
    Number
        Difference rounded toward negative infinity.
    """
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        mpfr_b = Number(b)
        return mpfr_a - mpfr_b

def sub_up(a: Number, b: Number) -> Number:
    """
    Subtract two numbers with upward directed rounding.

    Parameters
    ----------
    a : Number
        Minuend.
    b : Number
        Subtrahend.

    Returns
    -------
    Number
        Difference rounded toward positive infinity.
    """
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        mpfr_b = Number(b)
        return mpfr_a - mpfr_b

def mul_down(a: Number, b: Number) -> Number:
    """
    Multiply two numbers with downward directed rounding.

    Parameters
    ----------
    a : Number
        First factor.
    b : Number
        Second factor.

    Returns
    -------
    Number
        Product rounded toward negative infinity.
    """
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        mpfr_b = Number(b)
        return mpfr_a*mpfr_b

def mul_up(a: Number, b: Number):
    """
    Multiply two numbers with upward directed rounding.

    Parameters
    ----------
    a : Number
        First factor.
    b : Number
        Second factor.

    Returns
    -------
    Number
        Product rounded toward positive infinity.
    """
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        mpfr_b = Number(b)
        return mpfr_a*mpfr_b

def div_down(a: Number, b: Number):
    """
    Divide two numbers with downward directed rounding.

    Parameters
    ----------
    a : Number
        Numerator.
    b : Number
        Denominator.

    Returns
    -------
    Number
        Quotient rounded toward negative infinity.
    """
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        mpfr_b = Number(b)
        return mpfr_a / mpfr_b

def div_up(a: Number, b: Number):
    """
    Divide two numbers with upward directed rounding.

    Parameters
    ----------
    a : Number
        Numerator.
    b : Number
        Denominator.

    Returns
    -------
    Number
        Quotient rounded toward positive infinity.
    """
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        mpfr_b = Number(b)
        return mpfr_a / mpfr_b

def sqrt_up(a: Number):
    """
    Compute square root with upward directed rounding.

    Parameters
    ----------
    a : Number
        Input value.

    Returns
    -------
    Number
        Square root rounded toward positive infinity.
    """
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return sqrt(mpfr_a)

def sqrt_down(a: Number):
    """
    Compute square root with downward directed rounding.

    Parameters
    ----------
    a : Number
        Input value.

    Returns
    -------
    Number
        Square root rounded toward negative infinity.
    """
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return sqrt(mpfr_a)

def exp_up(a: Number):
    """
    Compute natural exponential with upward directed rounding.

    Parameters
    ----------
    a : Number
        Input exponent.

    Returns
    -------
    Number
        Exponential rounded toward positive infinity.
    """
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return exp(mpfr_a)

def exp_down(a: Number):
    """
    Compute natural exponential with downward directed rounding.

    Parameters
    ----------
    a : Number
        Input exponent.

    Returns
    -------
    Number
        Exponential rounded toward negative infinity.
    """
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return exp(mpfr_a)

def log_down(a: Number):
    """
    Compute natural logarithm with downward directed rounding.

    Parameters
    ----------
    a : Number
        Input value.

    Returns
    -------
    Number
        Natural logarithm rounded toward negative infinity.
    """
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return log(mpfr_a)

def log_up(a: Number):
    """
    Compute natural logarithm with upward directed rounding.

    Parameters
    ----------
    a : Number
        Input value.

    Returns
    -------
    Number
        Natural logarithm rounded toward positive infinity.
    """
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return log(mpfr_a)

def pow_up(a: Number, n: int):
    """
    Raise a number to an integer power with upward directed rounding.

    Parameters
    ----------
    a : Number
        Base value.
    n : int
        Integer exponent.

    Returns
    -------
    Number
        Power rounded toward positive infinity.
    """
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return mpfr_a ** n

def pow_down(a: Number, n: int):
    """
    Raise a number to an integer power with downward directed rounding.

    Parameters
    ----------
    a : Number
        Base value.
    n : int
        Integer exponent.

    Returns
    -------
    Number
        Power rounded toward negative infinity.
    """
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return mpfr_a ** n

def root_up(a: Number, n: int):
    """
    Compute the n-th root with upward directed rounding.

    Parameters
    ----------
    a : Number
        Input value.
    n : int
        Root degree.

    Returns
    -------
    Number
        n-th root rounded toward positive infinity.
    """
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return root(mpfr_a, int(n))

def root_down(a: Number, n: int):
    """
    Compute the n-th root with downward directed rounding.

    Parameters
    ----------
    a : Number
        Input value.
    n : int
        Root degree.

    Returns
    -------
    Number
        n-th root rounded toward negative infinity.
    """
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return root(mpfr_a, int(n))

def sin_up(a: Number):
    """
    Compute sine with upward directed rounding.

    Parameters
    ----------
    a : Number
        Angle in radians.

    Returns
    -------
    Number
        Sine rounded toward positive infinity.
    """
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return sin(mpfr_a)

def sin_down(a: Number):
    """
    Compute sine with downward directed rounding.

    Parameters
    ----------
    a : Number
        Angle in radians.

    Returns
    -------
    Number
        Sine rounded toward negative infinity.
    """
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return sin(mpfr_a)

def cos_down(a: Number):
    """
    Compute cosine with downward directed rounding.

    Parameters
    ----------
    a : Number
        Angle in radians.

    Returns
    -------
    Number
        Cosine rounded toward negative infinity.
    """
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return cos(mpfr_a)

def cos_up(a: Number):
    """
    Compute cosine with upward directed rounding.

    Parameters
    ----------
    a : Number
        Angle in radians.

    Returns
    -------
    Number
        Cosine rounded toward positive infinity.
    """
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return cos(mpfr_a)

def tan_up(a: Number):
    """
    Compute tangent with upward directed rounding.

    Parameters
    ----------
    a : Number
        Angle in radians.

    Returns
    -------
    Number
        Tangent rounded toward positive infinity.
    """
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return tan(mpfr_a)

def tan_down(a: Number):
    """
    Compute tangent with downward directed rounding.

    Parameters
    ----------
    a : Number
        Angle in radians.

    Returns
    -------
    Number
        Tangent rounded toward negative infinity.
    """
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return tan(mpfr_a)

def asin_up(a: Number):
    """
    Compute arcsine with upward directed rounding.

    Parameters
    ----------
    a : Number
        Input value.

    Returns
    -------
    Number
        Arcsine rounded toward positive infinity.
    """
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return asin(mpfr_a)

def asin_down(a: Number):
    """
    Compute arcsine with downward directed rounding.

    Parameters
    ----------
    a : Number
        Input value.

    Returns
    -------
    Number
        Arcsine rounded toward negative infinity.
    """
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return asin(mpfr_a)

def atan_down(a: Number):
    """
    Compute arctangent with downward directed rounding.

    Parameters
    ----------
    a : Number
        Input value.

    Returns
    -------
    Number
        Arctangent rounded toward negative infinity.
    """
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return atan(mpfr_a)

def atan_up(a: Number):
    """
    Compute arctangent with upward directed rounding.

    Parameters
    ----------
    a : Number
        Input value.

    Returns
    -------
    Number
        Arctangent rounded toward positive infinity.
    """
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return atan(mpfr_a)

def acos_up(a: Number):
    """
    Compute arccosine with upward directed rounding.

    Parameters
    ----------
    a : Number
        Input value.

    Returns
    -------
    Number
        Arccosine rounded toward positive infinity.
    """
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return acos(mpfr_a)

def acos_down(a: Number):
    """
    Compute arccosine with downward directed rounding.

    Parameters
    ----------
    a : Number
        Input value.

    Returns
    -------
    Number
        Arccosine rounded toward negative infinity.
    """
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return acos(mpfr_a)

def sinh_up(a: Number):
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return sinh(mpfr_a)

def sinh_down(a: Number):
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return sinh(mpfr_a)

def cosh_down(a: Number):
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return cosh(mpfr_a)

def cosh_up(a: Number):
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return cosh(mpfr_a)

def tanh_up(a: Number):
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return tanh(mpfr_a)

def tanh_down(a: Number):
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return tanh(mpfr_a)

def asinh_up(a: Number):
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return asinh(mpfr_a)

def asinh_down(a: Number):
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return asinh(mpfr_a)

def acosh_up(a: Number):
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return acosh(mpfr_a)

def acosh_down(a: Number):
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return acosh(mpfr_a)

def atanh_up(a: Number):
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return atanh(mpfr_a)

def atanh_down(a: Number):
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return atanh(mpfr_a)

def atan2_down(y: Number, x: Number):
    with context(get_context(), round = RoundDown):
        mpfr_x = Number(x)
        mpfr_y = Number(y)
        return atan2(mpfr_y, mpfr_x)

def atan2_up(y: Number, x: Number):
    with context(get_context(), round = RoundUp):
        mpfr_x = Number(x)
        mpfr_y = Number(y)
        return atan2(mpfr_y, mpfr_x)

def sqr_up(a: Number):
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return square(mpfr_a)

def sqr_down(a: Number):
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return square(mpfr_a)

def fma_up(a: Number, b: Number, c: Number):
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        mpfr_b = Number(b)
        mpfr_c = Number(c)
        return fma(mpfr_a, mpfr_b, mpfr_c)

def fma_down(a: Number, b: Number, c: Number):
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        mpfr_b = Number(b)
        mpfr_c = Number(c)
        return fma(mpfr_a, mpfr_b, mpfr_c)

def pow_up_interval(a: Number, n: Number):
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        mpfr_n = Number(n)
        return mpfr_a ** mpfr_n

def pow_down_interval(a: Number, n: Number):
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        mpfr_n = Number(n)
        return mpfr_a ** mpfr_n

def exp2_down(a: Number):
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return exp2(mpfr_a)

def exp2_up(a: Number):
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return exp2(mpfr_a)

def exp10_down(a: Number):
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return exp10(mpfr_a)

def exp10_up(a: Number):
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return exp10(mpfr_a)

def log2_down(a: Number):
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return log2(mpfr_a)

def log2_up(a: Number):
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return log2(mpfr_a)

def log10_down(a: Number):
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return log10(mpfr_a)

def log10_up(a: Number):
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return log10(mpfr_a)
