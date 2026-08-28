import pytest
from decoint import DecoratedInterval, acos, asin, atan, atan2, cos, sin, tan
from test_cases.test_exp_log_funcs import (
    test_acos,
    test_acos_dec,
    test_asin,
    test_asin_dec,
    test_atan,
    test_atan2,
    test_atan2_dec,
    test_atan_dec,
    test_cos,
    test_cos_dec,
    test_sin,
    test_sin_dec,
    test_tan,
    test_tan_dec,
)


@pytest.mark.parametrize("operand1, answer", test_sin)
def sin_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = sin(op1)
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)


@pytest.mark.parametrize("operand1, answer", test_sin_dec)
def sin_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = sin(op1)
    assert actual.is_nai == ans.is_nai
    if not ans.is_nai:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration


@pytest.mark.parametrize("operand1, answer", test_cos)
def cos_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = cos(op1)
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)


@pytest.mark.parametrize("operand1, answer", test_cos_dec)
def cos_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = cos(op1)
    assert actual.is_nai == ans.is_nai
    if not ans.is_nai:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration


@pytest.mark.parametrize("operand1, answer", test_tan)
def tan_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = tan(op1)
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)


@pytest.mark.parametrize("operand1, answer", test_tan_dec)
def tan_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = tan(op1)
    assert actual.is_nai == ans.is_nai
    if not ans.is_nai:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration


@pytest.mark.parametrize("operand1, answer", test_asin)
def asin_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = asin(op1)
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)


@pytest.mark.parametrize("operand1, answer", test_asin_dec)
def asin_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = asin(op1)
    assert actual.is_nai == ans.is_nai
    if not ans.is_nai:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration


@pytest.mark.parametrize("operand1, answer", test_acos)
def acos_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = acos(op1)
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)


@pytest.mark.parametrize("operand1, answer", test_acos_dec)
def acos_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = acos(op1)
    assert actual.is_nai == ans.is_nai
    if not ans.is_nai:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration


@pytest.mark.parametrize("operand1, answer", test_atan)
def atan_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = atan(op1)
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)


@pytest.mark.parametrize("operand1, answer", test_atan_dec)
def atan_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = atan(op1)
    assert actual.is_nai == ans.is_nai
    if not ans.is_nai:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration


@pytest.mark.parametrize("operand1, operand2, answer", test_atan2)
def atan2_testing(operand1, operand2, answer):
    op1 = DecoratedInterval(operand1)
    op2 = DecoratedInterval(operand2)
    ans = DecoratedInterval(answer)
    actual = atan2(op1, op2)
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)


@pytest.mark.parametrize("operand1, operand2, answer", test_atan2_dec)
def atan2_dec_testing(operand1, operand2, answer):
    op1 = DecoratedInterval(operand1)
    op2 = DecoratedInterval(operand2)
    ans = DecoratedInterval(answer)
    actual = atan2(op1, op2)
    assert actual.is_nai == ans.is_nai
    if not ans.is_nai:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration
