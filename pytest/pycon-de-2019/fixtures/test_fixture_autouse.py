import pytest


def create_test_db():
    pass


# conftest.py
@pytest.fixture(scope="session", autouse=True)
def db():
    db = create_test_db()
    return db
