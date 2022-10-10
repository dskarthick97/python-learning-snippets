import pytest


@pytest.mark.parametrize("arg1", [2, 4, 7])
def test_iseven(arg1):
    assert arg1 % 2 == 0


@pytest.mark.parametrize("arg1, arg2", [(1, 1), (2, 3), (3, 4)])
def test_successor(arg1, arg2):
    assert arg2 == arg1 + 1
