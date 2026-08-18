from decoint import DecoratedInterval, Interval
import pytest
from test_cases.test_set_ops import test_equal, test_equal_dec, test_subset, test_subset_dec, test_less, test_less_dec, test_precedes, test_precedes_dec, test_interior, test_interior_dec, test_strictly_less_than, test_strictly_less_than_dec, test_strictly_precedes, test_strictly_precedes_dec, test_disjoint, test_disjoint_dec

@pytest.mark.parametrize("operand1, operand2, answer", test_equal)
def equal_testing(operand1, operand2, answer):
    op1 = Interval(operand1)
    op2 = Interval(operand2)
    ans = bool(ans)
    actual = op1 == op2
    assert actual == ans

@pytest.mark.parametrize("operand1, operand2, answer", test_equal_dec)
def equal_dec_testing(operand1, operand2, answer):
    op1 = DecoratedInterval(operand1)
    op2 = DecoratedInterval(operand2)
    ans = bool(ans)
    actual = op1 == op2
    assert actual == ans

@pytest.mark.parametrize("operand1, operand2, answer", test_subset)
def subset_testing(operand1, operand2, answer):
    op1 = Interval(operand1)
    op2 = Interval(operand2)
    ans = bool(ans)
    actual = op1.subset(op2)
    assert actual == ans

@pytest.mark.parametrize("operand1, operand2, answer", test_subset_dec)
def subset_dec_testing(operand1, operand2, answer):
    op1 = DecoratedInterval(operand1)
    op2 = DecoratedInterval(operand2)
    ans = bool(ans)
    actual = op1.subset(op2)
    assert actual == ans

@pytest.mark.parametrize("operand1, operand2, answer", test_less)
def less_testing(operand1, operand2, answer):
    op1 = Interval(operand1)
    op2 = Interval(operand2)
    ans = bool(ans)
    actual = op1 < op2
    assert actual == ans

@pytest.mark.parametrize("operand1, operand2, answer", test_less_dec)
def less_dec_testing(operand1, operand2, answer):
    op1 = DecoratedInterval(operand1)
    op2 = DecoratedInterval(operand2)
    ans = bool(ans)
    actual = op1 < op2
    assert actual == ans

@pytest.mark.parametrize("operand1, operand2, answer", test_precedes)
def precedes_testing(operand1, operand2, answer):
    op1 = Interval(operand1)
    op2 = Interval(operand2)
    ans = bool(ans)
    actual = op1.precedes(op2)
    assert actual == ans

@pytest.mark.parametrize("operand1, operand2, answer", test_precedes_dec)
def precedes_dec_testing(operand1, operand2, answer):
    op1 = DecoratedInterval(operand1)
    op2 = DecoratedInterval(operand2)
    ans = bool(ans)
    actual = op1.precedes(op2)
    assert actual == ans

@pytest.mark.parametrize("operand1, operand2, answer", test_interior)
def interior_testing(operand1, operand2, answer):
    op1 = Interval(operand1)
    op2 = Interval(operand2)
    ans = bool(ans)
    actual = op1.interior(op2)
    assert actual == ans

@pytest.mark.parametrize("operand1, operand2, answer", test_interior_dec)
def interior_dec_testing(operand1, operand2, answer):
    op1 = DecoratedInterval(operand1)
    op2 = DecoratedInterval(operand2)
    ans = bool(ans)
    actual = op1.interior(op2)
    assert actual == ans

@pytest.mark.parametrize("operand1, operand2, answer", test_strictly_less_than)
def strictly_less_than_testing(operand1, operand2, answer):
    op1 = Interval(operand1)
    op2 = Interval(operand2)
    ans = bool(ans)
    actual = op1.strictly_less_than(op2)
    assert actual == ans

@pytest.mark.parametrize("operand1, operand2, answer", test_strictly_less_than_dec)
def strictly_less_than_dec_testing(operand1, operand2, answer):
    op1 = DecoratedInterval(operand1)
    op2 = DecoratedInterval(operand2)
    ans = bool(ans)
    actual = op1.strictly_less_than(op2)
    assert actual == ans

@pytest.mark.parametrize("operand1, operand2, answer", test_strictly_precedes)
def strictly_precedes_testing(operand1, operand2, answer):
    op1 = Interval(operand1)
    op2 = Interval(operand2)
    ans = bool(ans)
    actual = op1.strictly_precedes(op2)
    assert actual == ans

@pytest.mark.parametrize("operand1, operand2, answer", test_strictly_precedes_dec)
def strictly_precedes_dec_testing(operand1, operand2, answer):
    op1 = DecoratedInterval(operand1)
    op2 = DecoratedInterval(operand2)
    ans = bool(ans)
    actual = op1.strictly_precedes(op2)
    assert actual == ans

@pytest.mark.parametrize("operand1, operand2, answer", test_disjoint)
def disjoint_testing(operand1, operand2, answer):
    op1 = Interval(operand1)
    op2 = Interval(operand2)
    ans = bool(ans)
    actual = op1.disjoint(op2)
    assert actual == ans

@pytest.mark.parametrize("operand1, operand2, answer", test_disjoint_dec)
def disjoint_dec_testing(operand1, operand2, answer):
    op1 = DecoratedInterval(operand1)
    op2 = DecoratedInterval(operand2)
    ans = bool(ans)
    actual = op1.disjoint(op2)
    assert actual == ans
