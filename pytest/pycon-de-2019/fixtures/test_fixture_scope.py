import time
import pytest


@pytest.fixture(scope="module")
def fix():
    time.sleep(1)
    return 1


def test_func(fix):
    assert fix == 1


def test_func2(fix):
    assert fix == 1
