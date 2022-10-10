import pytest


@pytest.fixture(params=[10, 20])
def answer1(request):
    return 5 * request.param


@pytest.fixture
def answer2(answer1):
    return answer1 * 2


def test_answer(answer2):
    print(answer2)
