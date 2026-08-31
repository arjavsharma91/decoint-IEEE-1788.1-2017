import pytest
from decoint import DecoratedInterval, acosh, asinh, atanh, cosh, sinh, tanh
from testing.test_cases.test_hyperbolic_funcs import (
    test_acosh,
    test_acosh_dec,
    test_asinh,
    test_asinh_dec,
    test_atanh,
    test_atanh_dec,
    test_cosh,
    test_cosh_dec,
    test_sinh,
    test_sinh_dec,
    test_tanh,
    test_tanh_dec,
)


@pytest.mark.parametrize("operand1, answer", test_sinh)
def sinh_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = sinh(op1)
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)


@pytest.mark.parametrize("operand1, answer", test_cosh)
def cosh_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = cosh(op1)
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)


@pytest.mark.parametrize("operand1, answer", test_tanh)
def tanh_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = tanh(op1)
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)


@pytest.mark.parametrize("operand1, answer", test_sinh_dec)
def sinh_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = sinh(op1)
    assert actual.is_nai == ans.is_nai
    if not ans.is_nai:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration


@pytest.mark.parametrize("operand1, answer", test_cosh_dec)
def cosh_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = cosh(op1)
    assert actual.is_nai == ans.is_nai
    if not ans.is_nai:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration


@pytest.mark.parametrize("operand1, answer", test_tanh_dec)
def tanh_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = tanh(op1)
    assert actual.is_nai == ans.is_nai
    if not ans.is_nai:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration


@pytest.mark.parametrize("operand1, answer", test_asinh)
def asinh_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = asinh(op1)
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)


@pytest.mark.parametrize("operand1, answer", test_acosh)
def acosh_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = acosh(op1)
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)


@pytest.mark.parametrize("operand1, answer", test_atanh)
def atanh_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = atanh(op1)
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)


@pytest.mark.parametrize("operand1, answer", test_asinh_dec)
def asinh_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = asinh(op1)
    assert actual.is_nai == ans.is_nai
    if not ans.is_nai:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration


@pytest.mark.parametrize("operand1, answer", test_acosh_dec)
def acosh_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = acosh(op1)
    assert actual.is_nai == ans.is_nai
    if not ans.is_nai:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration


@pytest.mark.parametrize("operand1, answer", test_atanh_dec)
def atanh_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = atanh(op1)
    assert actual.is_nai == ans.is_nai
    if not ans.is_nai:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration
