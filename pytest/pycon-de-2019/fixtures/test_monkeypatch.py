import os
import sys
import pytest

# content of fixtures/test_monkeypatch.py
def test_one(monkeypatch):
    monkeypatch.setattr(sys, "platform", "toaster")
    monkeypatch.setenv("T", "ham")
    print("platform:", sys.platform)
    print("T:", os.environ["T"])
    assert False


def test_two():
    print("platform:", sys.platform)
    assert False
