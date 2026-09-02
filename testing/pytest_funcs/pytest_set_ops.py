import pytest
from decoint import DecoratedInterval, Interval
from testing.test_cases.test_set_ops import (
    test_hull,
    test_hull_dec,
    test_intersection,
    test_intersection_dec,
)


@pytest.mark.parametrize("operand1, operand2, answer", test_intersection)
def intersection_testing(operand1, operand2, answer):
    op1 = Interval(operand1)
    op2 = Interval(operand2)
    ans = Interval(answer)
    actual = op1.intersection(op2)
    assert actual.lo <= ans.lo
    assert actual.lo >= (ans.lo - 0.1)
    assert actual.hi >= ans.hi
    assert actual.hi <= (ans.hi + 0.1)


@pytest.mark.parametrize("operand1, operand2, answer", test_hull)
def hull_testing(operand1, operand2, answer):
    op1 = Interval(operand1)
    op2 = Interval(operand2)
    ans = Interval(answer)
    actual = op1.hull(op2)
    assert actual.lo <= ans.lo
    assert actual.lo >= (ans.lo - 0.1)
    assert actual.hi >= ans.hi
    assert actual.hi <= (ans.hi + 0.1)


@pytest.mark.parametrize("operand1, operand2, answer", test_hull_dec)
def hull_dec_testing(operand1, operand2, answer):
    op1 = DecoratedInterval(operand1)
    op2 = DecoratedInterval(operand2)
    ans = DecoratedInterval(answer)
    actual = op1.hull(op2)
    assert actual.is_nai == ans.is_nai
    if not ans.is_nai:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= (ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= (ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration


@pytest.mark.parametrize("operand1, operand2, answer", test_intersection_dec)
def intersection_dec_testing(operand1, operand2, answer):
    op1 = DecoratedInterval(operand1)
    op2 = DecoratedInterval(operand2)
    ans = DecoratedInterval(answer)
    actual = op1.intersection(op2)
    assert actual.is_nai == ans.is_nai
    if not ans.is_nai:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= (ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= (ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration
