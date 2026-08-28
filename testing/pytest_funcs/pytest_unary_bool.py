import pytest
from decoint import DecoratedInterval, Interval
from test_cases.test_unary_bool import (
    test_is_common,
    test_is_common_dec,
    test_is_empty,
    test_is_empty_dec,
    test_is_entire,
    test_is_entire_dec,
    test_is_singleton,
    test_is_singleton_dec,
)


@pytest.mark.parametrize("operand1, answer", test_is_empty)
def empty_testing(operand1, answer):
    op1 = Interval(operand1)
    ans = bool(answer)
    actual = op1.is_empty
    assert actual == ans


@pytest.mark.parametrize("operand1, answer", test_is_empty_dec)
def empty_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = bool(answer)
    actual = op1.is_empty
    assert actual == ans


@pytest.mark.parametrize("operand1, answer", test_is_entire)
def entire_testing(operand1, answer):
    op1 = Interval(operand1)
    ans = bool(answer)
    actual = op1.is_entire
    assert actual == ans


@pytest.mark.parametrize("operand1, answer", test_is_entire_dec)
def entire_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = bool(answer)
    actual = op1.is_entire
    assert actual == ans


@pytest.mark.parametrize("operand1, answer", test_is_common)
def common_testing(operand1, answer):
    op1 = Interval(operand1)
    ans = bool(answer)
    actual = op1.is_common
    assert actual == ans


@pytest.mark.parametrize("operand1, answer", test_is_common_dec)
def common_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = bool(answer)
    actual = op1.is_common
    assert actual == ans


@pytest.mark.parametrize("operand1, answer", test_is_singleton)
def singleton_testing(operand1, answer):
    op1 = Interval(operand1)
    ans = bool(answer)
    actual = op1.is_singleton
    assert actual == ans


@pytest.mark.parametrize("operand1, answer", test_is_singleton_dec)
def singleton_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = bool(answer)
    actual = op1.is_singleton
    assert actual == ans
