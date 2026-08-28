import pytest
from decoint import DecoratedInterval
from gmpy2 import mpfr
from test_cases.test_unary_properties import (
    test_inf,
    test_inf_dec,
    test_magnitude,
    test_magnitude_dec,
    test_midpoint,
    test_midpoint_dec,
    test_mignitude,
    test_mignitude_dec,
    test_radius,
    test_radius_dec,
    test_sup,
    test_sup_dec,
    test_width,
    test_width_dec,
)


@pytest.mark.parametrize("operand1, answer", test_inf)
def inf_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = mpfr(answer)
    actual = op1.inf
    assert actual == ans


@pytest.mark.parametrize("operand1, answer", test_inf_dec)
def inf_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = mpfr(answer)
    actual = op1.inf
    assert actual == ans


@pytest.mark.parametrize("operand1, answer", test_sup)
def sup_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = mpfr(answer)
    actual = op1.sup
    assert actual == ans


@pytest.mark.parametrize("operand1, answer", test_sup_dec)
def sup_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = mpfr(answer)
    actual = op1.sup
    assert actual == ans


@pytest.mark.parametrize("operand1, answer", test_midpoint)
def midpoint_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = mpfr(answer)
    actual = op1.midpoint
    assert actual == ans


@pytest.mark.parametrize("operand1, answer", test_midpoint_dec)
def midpoint_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = mpfr(answer)
    actual = op1.midpoint
    assert actual == ans


@pytest.mark.parametrize("operand1, answer", test_radius)
def radius_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = mpfr(answer)
    actual = op1.radius
    assert actual == ans


@pytest.mark.parametrize("operand1, answer", test_radius_dec)
def radius_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = mpfr(answer)
    actual = op1.radius
    assert actual == ans


@pytest.mark.parametrize("operand1, answer", test_width)
def width_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = mpfr(answer)
    actual = op1.width
    assert actual == ans


@pytest.mark.parametrize("operand1, answer", test_width_dec)
def width_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = mpfr(answer)
    actual = op1.width
    assert actual == ans


@pytest.mark.parametrize("operand1, answer", test_magnitude)
def magnitude_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = mpfr(answer)
    actual = op1.magnitude
    assert actual == ans


@pytest.mark.parametrize("operand1, answer", test_magnitude_dec)
def magnitude_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = mpfr(answer)
    actual = op1.magnitude
    assert actual == ans


@pytest.mark.parametrize("operand1, answer", test_mignitude)
def mignitude_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = mpfr(answer)
    actual = op1.mignitude
    assert actual == ans


@pytest.mark.parametrize("operand1, answer", test_mignitude_dec)
def mignitude_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = mpfr(answer)
    actual = op1.mignitude
    assert actual == ans
