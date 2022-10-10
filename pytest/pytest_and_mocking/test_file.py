import pytest

# Exception
def plusone(x):
    return x + 1


def test_plusone():
    with pytest.raises(AssertionError):
        assert plusone(3) == 5


# Fixture example
class Person:
    @staticmethod
    def greet():
        return "Hello there!"


@pytest.fixture
def person():
    return Person()


def test_greet(person):
    greeting = person.greet()
    assert greeting == "Hi there!"


# Verifying calls - Mocking and stubbing
## 1. Mocking
class DB:
    def __init__(self):
        pass

    def persist(self, animal):
        pass


class Animal:
    def __init__(self, name, db):
        self.name = name
        self.db = db

    def save(self):
        self.db.persist(self)


# Here I want to test whether the animal save interacts with the db's persist function
from mock import Mock


@pytest.fixture
def mock_db():
    return Mock(spec=DB)


# passes
def test_save_persists_to_db(mock_db):
    venom = Animal("Venom", mock_db)
    venom.save()
    mock_db.persist.assert_called_with(venom)


# fails
def test_fail_not_called(mock_db):
    mock_db.persist.assert_called_with()
    # E AssertionError: Expected call: persist()
    # E Not called


def test_fail_called_with_other_arg(mock_db):
    mock_db.persist(1, 2, 3)
    mock_db.persist.assert_called_with()
    # E AssertionError: Expected call: persist()
    # E Actual call: persist(1, 2, 3)


def test_any_call(mock_db):
    mock_db.persist(1)
    mock_db.persist(2)
    mock_db.persist.assert_any_call(1)  # Passes


## 2. Stubbing - return values

import random


class WeatherService:
    def barometer(self):
        # some unpredictable result here (live weather)
        return random.choice(["rising", "falling"])


class Forecaster:
    def __init__(self, weather_service):
        self.weather_service = weather_service

    def forecast(self):
        reading = self.weather_service.barometer()
        forecasts = dict(
            rising="Going to rain",
            falling="Looks clear",
        )
        return forecasts[reading]


@pytest.fixture
def mock_ws():
    return Mock(spec=WeatherService)


def test_rain_when_barometer_rising(mock_ws):
    forecaster = Forecaster(mock_ws)
    mock_ws.barometer.return_value = "rising"  # stubbing the return value
    assert forecaster.forecast() == "Going to rain"


def test_rain_when_barometer_falling(mock_ws):
    forecaster = Forecaster(mock_ws)
    mock_ws.barometer.return_value = "falling"  # stubbing the return value
    assert forecaster.forecast() == "Looks clear"


# Since there are some repeated code, we can refactor them to use a parameterized test
@pytest.mark.parametrize(
    "reading, expected_forecast",
    [
        ("rising", "Going to rain"),
        ("falling", "Looks clear"),
    ],
)
def test_forecast(reading, expected_forecast, mock_ws):
    forecaster = Forecaster(mock_ws)
    mock_ws.barometer.return_value = reading
    assert forecaster.forecast() == expected_forecast


# Monkeypatching
## Take the same weather service example. Let's have the Forecaster class as
class AnotherForecaster:
    def __init__(self):
        self.weather_service = WeatherService()
        # here i won't be able to inject a mock into the constructor

    def forecast(self):
        reading = self.weather_service.barometer()
        forecasts = dict(
            rising="Going to rain",
            falling="Looks clear",
        )
        return forecasts[reading]


# monkeypatch to the rescue
## - it is a special predefined fixture
## - use monkeypatch.setattr() to go in to a module and patch a value
## - pytest removes the patch when the test function returns
def test_rain_when_barometer_rising_mp(monkeypatch, mock_ws):
    WS = Mock(return_value=mock_ws)  # stubbed return value
    monkeypatch.setattr("WeatherService", WS)
    forecaster = AnotherForecaster()
    mock_ws.barometer.return_value = "rising"
    assert forecaster.forecast() == "Going to rain"


# Plugins
## 1. Invoke the python debugger for each failure - pytest <test-file> --pdb
## 2. Debug first failure, then stop running tests - pytest <test-file> -x --pdb


# Tip
class Developer:
    def __init__(self, favourite):
        self.loves = favourite

    def brag(self):
        return self.loves + " is the best!"


@pytest.fixture
def language():
    return "Python"


@pytest.fixture
def developer(language):
    return Developer(language)


def test_brag(developer):
    assert developer.brag() == "Python is the best!"


# what if want to make this developer instance love another language instead?
# 1. Parameterize dependent fixtures
@pytest.mark.parametrize("language", ["JavaScript"])
def test_brag_works_for_js(developer):
    assert developer.brag() == "JavaScript is the best!"
