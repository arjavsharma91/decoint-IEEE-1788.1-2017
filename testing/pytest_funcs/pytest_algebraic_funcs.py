import pytest
from decoint import DecoratedInterval, Interval, pow_int, pow_interval, sqr, sqrt
from testing.test_cases.test_algebraic_funcs import (
    test_pow_int,
    test_pow_int_dec,
    test_pow_interval,
    test_pow_interval_dec,
    test_sqr,
    test_sqr_dec,
    test_sqrt,
    test_sqrt_dec,
)


@pytest.mark.parametrize("operand1, answer", test_sqr)
def sqr_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = sqr(op1)
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= ans.interval.lo - 0.1
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= (ans.interval.hi + 0.1)


@pytest.mark.parametrize("operand1, answer", test_sqrt)
def sqrt_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = sqrt(op1)
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= (ans.interval.lo - 0.1)
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= (ans.interval.hi + 0.1)


@pytest.mark.parametrize("operand1, answer", test_sqr_dec)
def sqr_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = sqr(op1)
    assert actual.is_nai == ans.is_nai
    if not ans.is_nai:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= (ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= (ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration


@pytest.mark.parametrize("operand1, answer", test_sqrt_dec)
def sqrt_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = sqrt(op1)
    assert actual.is_nai == ans.is_nai
    if not ans.is_nai:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= (ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= (ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration


@pytest.mark.parametrize("operand1, operand2, answer", test_pow_int)
def pow_int_testing(operand1, operand2, answer):
    op1 = DecoratedInterval(operand1)
    op2 = int(operand2)
    ans = DecoratedInterval(answer)
    actual = pow_int(op1, op2)
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= (ans.interval.lo - 0.1)
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= (ans.interval.hi + 0.1)


@pytest.mark.parametrize("operand1, operand2, answer", test_pow_interval)
def pow_interval_testing(operand1, operand2, answer):
    op1 = DecoratedInterval(operand1)
    op2 = DecoratedInterval(operand2)
    ans = DecoratedInterval(answer)
    actual = pow_interval(op1, op2)
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= (ans.interval.lo - 0.1)
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= (ans.interval.hi + 0.1)


@pytest.mark.parametrize("operand1, operand2, answer", test_pow_interval_dec)
def pow_interval_dec_testing(operand1, operand2, answer):
    op1 = DecoratedInterval(operand1)
    op2 = DecoratedInterval(operand2)
    ans = DecoratedInterval(answer)
    actual = pow_interval(op1, op2)
    assert actual.is_nai == ans.is_nai
    if not ans.is_nai:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= (ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= (ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration


@pytest.mark.parametrize("operand1, operand2, answer", test_pow_int_dec)
def pow_int_dec_testing(operand1, operand2, answer):
    op1 = DecoratedInterval(operand1)
    op2 = int(operand2)
    ans = DecoratedInterval(answer)
    actual = pow_int(op1, op2)
    assert actual.is_nai == ans.is_nai
    if not ans.is_nai:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= (ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= (ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration
