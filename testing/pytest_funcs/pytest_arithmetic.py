import pytest
from decoint import DecoratedInterval, Interval, fma, reciprocal
from testing.test_cases.test_arithmetic_cases import (
    add_dec_test,
    add_test,
    div_dec_test,
    div_test,
    fma_test,
    mul_dec_test,
    mul_test,
    neg_dec_test,
    neg_test,
    recip_dec_test,
    recip_test,
    sub_dec_test,
    sub_test,
)


@pytest.mark.parametrize("operand1, operand2, answer", add_test)
def addition_testing(operand1, operand2, answer):
    op1 = Interval(operand1)
    op2 = Interval(operand2)
    ans = Interval(answer)
    actual = op1 + op2
    assert actual.lo <= ans.lo
    assert actual.lo >= pytest.approx(ans.lo - 0.1)
    assert actual.hi >= ans.hi
    assert actual.hi <= pytest.approx(ans.hi + 0.1)


@pytest.mark.parametrize("operand1, operand2, answer", sub_test)
def subtraction_testing(operand1, operand2, answer):
    op1 = Interval(operand1)
    op2 = Interval(operand2)
    ans = Interval(answer)
    actual = op1 - op2
    assert actual.lo <= ans.lo
    assert actual.lo >= pytest.approx(ans.lo - 0.1)
    assert actual.hi >= ans.hi
    assert actual.hi <= pytest.approx(ans.hi + 0.1)


@pytest.mark.parametrize("operand1, operand2, answer", mul_test)
def multiplication_testing(operand1, operand2, answer):
    op1 = Interval(operand1)
    op2 = Interval(operand2)
    ans = Interval(answer)
    actual = op1 * op2
    assert actual.lo <= ans.lo
    assert actual.lo >= pytest.approx(ans.lo - 0.1)
    assert actual.hi >= ans.hi
    assert actual.hi <= pytest.approx(ans.hi + 0.1)


@pytest.mark.parametrize("operand1, operand2, answer", div_test)
def division_testing(operand1, operand2, answer):
    op1 = Interval(operand1)
    op2 = Interval(operand2)
    ans = Interval(answer)
    actual = op1 / op2
    assert actual.lo <= ans.lo
    assert actual.lo >= pytest.approx(ans.lo - 0.1)
    assert actual.hi >= ans.hi
    assert actual.hi <= pytest.approx(ans.hi + 0.1)


@pytest.mark.parametrize("operand1, operand2, answer", add_dec_test)
def addition_dec_testing(operand1, operand2, answer):
    op1 = DecoratedInterval(operand1)
    op2 = DecoratedInterval(operand2)
    ans = DecoratedInterval(answer)
    actual = op1 + op2
    assert actual.is_nai == ans.is_nai
    if not ans.is_nai:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration


@pytest.mark.parametrize("operand1, operand2, answer", div_dec_test)
def division_dec_testing(operand1, operand2, answer):
    op1 = DecoratedInterval(operand1)
    op2 = DecoratedInterval(operand2)
    ans = DecoratedInterval(answer)
    actual = op1 / op2
    assert actual.is_nai == ans.is_nai
    if not ans.is_nai:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration


@pytest.mark.parametrize("operand1, operand2, answer", sub_dec_test)
def subtraction_dec_testing(operand1, operand2, answer):
    op1 = DecoratedInterval(operand1)
    op2 = DecoratedInterval(operand2)
    ans = DecoratedInterval(answer)
    actual = op1 - op2
    assert actual.is_nai == ans.is_nai
    if not ans.is_nai:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration


@pytest.mark.parametrize("operand1, operand2, answer", mul_dec_test)
def multiplication_dec_testing(operand1, operand2, answer):
    op1 = DecoratedInterval(operand1)
    op2 = DecoratedInterval(operand2)
    ans = DecoratedInterval(answer)
    actual = op1 * op2
    assert actual.is_nai == ans.is_nai
    if not ans.is_nai:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration


@pytest.mark.parametrize("operand1, answer", recip_dec_test)
def recip_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = reciprocal(op1)
    assert actual.is_nai == ans.is_nai
    if not ans.is_nai:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration


@pytest.mark.parametrize("operand1, answer", recip_test)
def recip_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = reciprocal(op1)
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)


@pytest.mark.parametrize("operand1, answer", neg_dec_test)
def neg_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = -op1
    assert actual.is_nai == ans.is_nai
    if not ans.is_nai:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration


@pytest.mark.parametrize("operand1, answer", neg_test)
def neg_testing(operand1, answer):
    op1 = Interval(operand1)
    ans = Interval(answer)
    actual = -op1
    assert actual.lo <= ans.lo
    assert actual.lo >= pytest.approx(ans.lo - 0.1)
    assert actual.hi >= ans.hi
    assert actual.hi <= pytest.approx(ans.hi + 0.1)


@pytest.mark.parametrize("operand1, operand2, operand3, answer", fma_test)
def fma_testing(operand1, operand2, operand3, answer):
    op1 = Interval(operand1)
    op2 = Interval(operand2)
    op3 = Interval(operand3)
    ans = Interval(answer)
    actual = fma(op1, op2, op3)
    assert actual.lo <= ans.lo
    assert actual.lo >= pytest.approx(ans.lo - 0.1)
    assert actual.hi >= ans.hi
    assert actual.hi <= pytest.approx(ans.hi + 0.1)

