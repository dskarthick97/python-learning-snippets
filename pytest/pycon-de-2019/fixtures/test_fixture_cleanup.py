import pytest

class A(object):

    def __init__(self):
        print("A: setup")

    def finish(self):
        print("A: teardown")

@pytest.fixture
def fix():
    a = A()
    yield a
    a.finish()

def test_fix(fix):
    print("in the test")
