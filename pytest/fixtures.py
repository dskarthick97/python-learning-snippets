import pytest


# Requesting Fixtures
class Fruit:
    def __init__(self, name):
        self.name = name
        self.cubed = False

    def cube(self):
        self.cubed = True


class FruitSalad:
    def __init__(self, *fruit_bowl):
        self.fruits = fruit_bowl
        self._cube_fruit()

    def _cube_fruit(self):
        for fruit in self.fruits:
            fruit.cube()


@pytest.fixture
def fruit_bowl():
    return [Fruit("apple"), Fruit("grape")]


def test_fruit_salad(fruit_bowl):
    fruit_salad = FruitSalad(*fruit_bowl)

    assert all(fruit.cubed for fruit in fruit_salad.fruits)


# Fixtures can request other fixtures
@pytest.fixture
def first_entry():
    return "venom"


@pytest.fixture
def order(first_entry):
    return [first_entry]


def test_string(order):
    order.append(" - let there be carnage")

    assert order == ["venom", " - let there be carnage"]


# Fixtures are reusable
def test_another_string(order):
    order.append(" - maximum carnage")

    assert order == ["venom", " - maximum carnage"]


# A test / fixture can request more than one fixture at a time.
@pytest.fixture
def second_entry():
    return "spider-man"


@pytest.fixture
def another_order(first_entry, second_entry):
    return [first_entry, second_entry]


@pytest.fixture
def expected_list():
    return ["venom", "spider-man", "multi-verse"]


def test_multiverse_string(another_order, expected_list):
    another_order.append("multi-verse")

    assert another_order == expected_list


# Fixtures can be requested more than once per test (return values are cached)
@pytest.fixture
def empty_order():
    return []


@pytest.fixture
def append_first(empty_order, first_entry):
    return empty_order.append(first_entry)


def test_string_only(append_first, empty_order, first_entry):
    assert empty_order == [first_entry]


# Autouse fixtures (fixtures you don't have to request)
@pytest.fixture(autouse=True)
def append_first_(empty_order, first_entry):
    return empty_order.append(first_entry)


def test_string_only_(empty_order, first_entry):
    assert empty_order == [first_entry]


# Scope: sharing fixtures across classes, modules, packages or session

# Fixtures can introspect the requesting test context
