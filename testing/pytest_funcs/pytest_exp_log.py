import pytest
from decoint import DecoratedInterval, exp, exp2, exp10, log, log2, log10
from testing.test_cases.test_exp_log_funcs import (
    test_exp,
    test_exp_dec,
    test_exp2,
    test_exp2_dec,
    test_exp10,
    test_exp10_dec,
    test_log,
    test_log_dec,
    test_log2,
    test_log2_dec,
    test_log10,
    test_log10_dec,
)


@pytest.mark.parametrize("operand1, answer", test_exp)
def exp_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = exp(op1)
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)


@pytest.mark.parametrize("operand1, answer", test_exp10)
def exp10_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = exp10(op1)
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)


@pytest.mark.parametrize("operand1, answer", test_exp2)
def exp2_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = exp2(op1)
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)


@pytest.mark.parametrize("operand1, answer", test_log)
def log_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = log(op1)
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)


@pytest.mark.parametrize("operand1, answer", test_log2)
def log2_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = log2(op1)
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)


@pytest.mark.parametrize("operand1, answer", test_log10)
def log10_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = log10(op1)
    assert actual.interval.lo <= ans.interval.lo
    assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
    assert actual.interval.hi >= ans.interval.hi
    assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)


@pytest.mark.parametrize("operand1, answer", test_log_dec)
def log_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = log(op1)
    assert actual.is_nai == ans.is_nai
    if not ans.is_nai:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration


@pytest.mark.parametrize("operand1, answer", test_log2_dec)
def log2_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = log2(op1)
    assert actual.is_nai == ans.is_nai
    if not ans.is_nai:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration


@pytest.mark.parametrize("operand1, answer", test_log10_dec)
def log10_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = log10(op1)
    assert actual.is_nai == ans.is_nai
    if not ans.is_nai:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration


@pytest.mark.parametrize("operand1, answer", test_exp_dec)
def exp_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = exp(op1)
    assert actual.is_nai == ans.is_nai
    if not ans.is_nai:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration


@pytest.mark.parametrize("operand1, answer", test_exp2_dec)
def exp2_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = exp2(op1)
    assert actual.is_nai == ans.is_nai
    if not ans.is_nai:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration


@pytest.mark.parametrize("operand1, answer", test_exp10_dec)
def exp10_dec_testing(operand1, answer):
    op1 = DecoratedInterval(operand1)
    ans = DecoratedInterval(answer)
    actual = exp10(op1)
    assert actual.is_nai == ans.is_nai
    if not ans.is_nai:
        assert actual.interval.lo <= ans.interval.lo
        assert actual.interval.lo >= pytest.approx(ans.interval.lo - 0.1)
        assert actual.interval.hi >= ans.interval.hi
        assert actual.interval.hi <= pytest.approx(ans.interval.hi + 0.1)
        assert actual.decoration == ans.decoration



