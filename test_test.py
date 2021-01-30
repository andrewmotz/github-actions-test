# Test file

from test import sum

def test_sum_pos() -> None:
    assert sum(1,1) == 2
    

def test_sum_zero() -> None:
    assert sum(1,-1) == 0

def test_sum_neg() -> None:
    assert sum(-1,-1) == -2