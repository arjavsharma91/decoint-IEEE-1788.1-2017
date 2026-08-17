import decoint
from test_cases.test_arithmetic import add_test
import pytest

@pytest.mark.parametrize("operand1, operand2, answer", add_test)
def addition_testing(operand1, operand2, answer):
    op1 = Interval(operand1)
    op2 = Interval(operand2)
    ans = Interval(ans)
    actual = op1 + op2
    assert actual.lo <= ans.lo
    assert actual.lo >= pytest.approx(ans.lo - 0.1)
    assert actual.hi >= ans.hi
    assert actual.hi <= pytest.approx(ans.hi + 0.1)

@pytest.mark.parametrize("operand1, operand2, answer", sub_test)
def subtraction_testing(operand1, operand2, answer):
    op1 = Interval(operand1)
    op2 = Interval(operand2)
    ans = Interval(ans)
    actual = op1 - op2
    assert actual.lo <= ans.lo
    assert actual.lo >= pytest.approx(ans.lo - 0.1)
    assert actual.hi >= ans.hi
    assert actual.hi <= pytest.approx(ans.hi + 0.1)

@pytest.mark.parametrize("operand1, operand2, answer", mul_test)
def multiplication_testing(operand1, operand2, answer):
    op1 = Interval(operand1)
    op2 = Interval(operand2)
    ans = Interval(ans)
    actual = op1 * op2
    assert actual.lo <= ans.lo
    assert actual.lo >= pytest.approx(ans.lo - 0.1)
    assert actual.hi >= ans.hi
    assert actual.hi <= pytest.approx(ans.hi + 0.1)

@pytest.mark.parametrize("operand1, operand2, answer", div_test)
def division_testing(operand1, operand2, answer):
    op1 = Interval(operand1)
    op2 = Interval(operand2)
    ans = Interval(ans)
    actual = op1 / op2
    assert actual.lo <= ans.lo
    assert actual.lo >= pytest.approx(ans.lo - 0.1)
    assert actual.hi >= ans.hi
    assert actual.hi <= pytest.approx(ans.hi + 0.1)

@pytest.mark.parametrize("operand1, operand2, answer", add_dec_test)
def addition_dec_testing(operand1, operand2, answer):
    op1 = DecoratedInterval(operand1)
    op2 = DecoratedInterval(operand2)
    ans = DecoratedInterval(ans)
    actual = op1 + op2
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
    assert actual.decoration == ans.decoration

@pytest.mark.parametrize("operand1, operand2, answer", div_dec_test)
def division_dec_testing(operand1, operand2, answer):
    op1 = DecoratedInterval(operand1)
    op2 = DecoratedInterval(operand2)
    ans = DecoratedInterval(ans)
    actual = op1 / op2
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
    assert actual.decoration == ans.decoration

@pytest.mark.parametrize("operand1, operand2, answer", sub_dec_test)
def subtraction_dec_testing(operand1, operand2, answer):
    op1 = DecoratedInterval(operand1)
    op2 = DecoratedInterval(operand2)
    ans = DecoratedInterval(ans)
    actual = op1 - op2
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
    assert actual.decoration == ans.decoration

@pytest.mark.parametrize("operand1, operand2, answer", mul_dec_test)
def division_dec_testing(operand1, operand2, answer):
    op1 = DecoratedInterval(operand1)
    op2 = DecoratedInterval(operand2)
    ans = DecoratedInterval(ans)
    actual = op1 * op2
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
    assert actual.decoration == ans.decoration
