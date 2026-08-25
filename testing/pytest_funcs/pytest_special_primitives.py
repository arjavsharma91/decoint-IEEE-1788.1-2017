from decoint import DecoratedInterval, Interval, sing, ceil, trunc, abs
import pytest
from test_cases.test_set_ops import test_sign, test_sign_dec, test_ceil, test_ceil_dec, test_floor, test_floor_dec, test_trunc, test_trunc_dec, test_abs, test_abs_dec

@pytest.mark.parametrize("operand1, answer", test_sign)
def sign_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(ans)
    actual = sign(op1)
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)

@pytest.mark.parametrize("operand1, answer", test_sign_dec)
def sign_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(ans)
    actual = sign(op1)
    if ans.is_nai and actual.is_nai:
        assert 1 == 1
    else:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration

@pytest.mark.parametrize("operand1, answer", test_ceil)
def ceil_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(ans)
    actual = ceil(op1)
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)

@pytest.mark.parametrize("operand1, answer", test_ceil_dec)
def ceil_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(ans)
    actual = ceil(op1)
    if ans.is_nai and actual.is_nai:
        assert 1 == 1
    else:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration

@pytest.mark.parametrize("operand1, answer", test_floor)
def floor_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(ans)
    actual = floor(op1)
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)

@pytest.mark.parametrize("operand1, answer", test_floor_dec)
def floor_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(ans)
    actual = floor(op1)
    if ans.is_nai and actual.is_nai:
        assert 1 == 1
    else:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration

@pytest.mark.parametrize("operand1, answer", test_trunc)
def trunc_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(ans)
    actual = trunc(op1)
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)

@pytest.mark.parametrize("operand1, answer", test_trunc_dec)
def trunc_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(ans)
    actual = trunc(op1)
    if ans.is_nai and actual.is_nai:
        assert 1 == 1
    else:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration

@pytest.mark.parametrize("operand1, answer", test_abs)
def abs_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(ans)
    actual = abs(op1)
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)

@pytest.mark.parametrize("operand1, answer", test_abs_dec)
def abs_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(ans)
    actual = abs(op1)
    if ans.is_nai and actual.is_nai:
        assert 1 == 1
    else:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration
