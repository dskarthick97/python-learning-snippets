import pytest


def divide(x, y):
    return x / y


def test_sample():
    assert 4 == 4


def test_raises():
    with pytest.raises(ZeroDivisionError):
        divide(3, 0)
