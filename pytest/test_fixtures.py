import pytest


@pytest.fixture(
    scope="module",
    params=["Venom", "Venom - Let there be Carnage!"],
)
def somevalue(request):
    print("Inside somevalue function...")
    return request.param


@pytest.mark.parametrize(
    "expected_result",
    ["Venom", "Venom - Let there be Carnage!"],
)
def test_venom_title(somevalue, expected_result):
    assert somevalue == expected_result


# def test_venom_sequel(somevalue):
#     assert "Venom" == somevalue
