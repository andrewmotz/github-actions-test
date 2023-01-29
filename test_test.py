# Test file
import pytest
from test import sum, divide

def test_sum_pos() -> None:
    assert sum(1,1) == 2

def test_sum_zero() -> None:
    assert sum(1,-1) == 0

def test_sum_neg() -> None:
    assert sum(-1,-1) == -2

def test_divide_by_zero() -> None:
    with pytest.raises(ZeroDivisionError):
        divide(1,0)