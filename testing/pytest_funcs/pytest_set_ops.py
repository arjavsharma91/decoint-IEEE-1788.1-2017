from decoint import DecoratedInterval, Interval
import pytest
from test_cases.test_set_ops import test_intersection, test_intersection_dec, test_hull, test_hull_dec

@pytest.mark.parametrize("operand1, operand2, answer", test_intersection)
def intersection_testing(operand1, operand2, answer):
    op1 = Interval(operand1)
    op2 = Interval(operand2)
    ans = Interval(ans)
    actual = op1.intersection(op2)
    assert actual.lo <= ans.lo
    assert actual.lo >= pytest.approx(ans.lo - 0.1)
    assert actual.hi >= ans.hi
    assert actual.hi <= pytest.approx(ans.hi + 0.1)

@pytest.mark.parametrize("operand1, operand2, answer", test_hull)
def hull_testing(operand1, operand2, answer):
    op1 = Interval(operand1)
    op2 = Interval(operand2)
    ans = Interval(ans)
    actual = op1.hull(op2)
    assert actual.lo <= ans.lo
    assert actual.lo >= pytest.approx(ans.lo - 0.1)
    assert actual.hi >= ans.hi
    assert actual.hi <= pytest.approx(ans.hi + 0.1)

@pytest.mark.parametrize("operand1, operand2, answer", test_hull_dec)
def hull_dec_testing(operand1, operand2, answer):
    op1 = DecoratedInterval(operand1)
    op2 = DecoratedInterval(operand2)
    ans = DecoratedInterval(ans)
    actual = op1.hull(op2)
    if ans.is_nai and actual.is_nai:
        assert 1 == 1
    else:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration

@pytest.mark.parametrize("operand1, operand2, answer", test_intersection_dec)
def intersection_dec_testing(operand1, operand2, answer):
    op1 = DecoratedInterval(operand1)
    op2 = DecoratedInterval(operand2)
    ans = DecoratedInterval(ans)
    actual = op1.intersection(op2)
    if ans.is_nai and actual.is_nai:
        assert 1 == 1
    else:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration
