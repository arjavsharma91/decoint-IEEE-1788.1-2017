from decoint import interval_max, interval_min, DecoratedInterval, Interval
import pytest
from test_cases.test_exp_log_funcs import test_interval_max, test_interval_min, test_interval_max_dec, test_interval_min_dec

@pytest.mark.parametrize("operand1, operand2, answer", test_interval_max)
def interval_max_testing(operand1, operand2, answer):
    op1 = DecoratedInterval(operand1)
    op2 = DecoratedInterval(operand2)
    ans = DecoratedInterval(ans)
    actual = interval_max(op1, op2)
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)

@pytest.mark.parametrize("operand1, operand2, answer", test_interval_max_dec)
def interval_max_dec_testing(operand1, operand2, answer):
    op1 = DecoratedInterval(operand1)
    op2 = DecoratedInterval(operand2)
    ans = DecoratedInterval(ans)
    actual = interval_max(op1, op2)
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
    assert actual.decoration == ans.decoration

@pytest.mark.parametrize("operand1, operand2, answer", test_interval_min)
def interval_min_testing(operand1, operand2, answer):
    op1 = DecoratedInterval(operand1)
    op2 = DecoratedInterval(operand2)
    ans = DecoratedInterval(ans)
    actual = interval_min(op1, op2)
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)

@pytest.mark.parametrize("operand1, operand2, answer", test_interval_min_dec)
def interval_min_dec_testing(operand1, operand2, answer):
    op1 = DecoratedInterval(operand1)
    op2 = DecoratedInterval(operand2)
    ans = DecoratedInterval(ans)
    actual = interval_min(op1, op2)
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
    assert actual.decoration == ans.decoration
