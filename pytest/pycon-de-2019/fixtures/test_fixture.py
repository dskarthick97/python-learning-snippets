import pytest


@pytest.fixture
def somevalue():
    pytest.skip("test")  # for skipping the fixture injection
    return 42


def test_function(somevalue):
    assert somevalue == 42
