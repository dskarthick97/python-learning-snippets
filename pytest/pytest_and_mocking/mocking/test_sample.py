import pytest
import requests_mock
import unittest.mock as mock

from sample import guess_number
import sample_requests


@pytest.mark.parametrize(
    "input_, expected",
    [
        (3, "You won!"),
        (4, "You lost!"),
    ],
)
@mock.patch("sample.roll_dice")
def test_guess_number(mock_roll_dice, input_, expected):
    mock_roll_dice.return_value = 3
    assert guess_number(input_) == expected
    mock_roll_dice.assert_called_once()


@mock.patch("sample_requests.requests.get")
def test_get_res(mock_requests_get):
    mock_requests_get.return_value.status_code = 500
    assert sample_requests.get_res() == 500
    mock_requests_get.assert_called_once()
