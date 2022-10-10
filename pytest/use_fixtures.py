import pytest


@pytest.fixture(scope="module")
def simple_fixture():
    return 42


# @pytest.mark.usefixtures("simple_fixture")
class TestFixture:
    def test_something(self, simple_fixture):
        assert simple_fixture == 42
