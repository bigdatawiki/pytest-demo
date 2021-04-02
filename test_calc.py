import calc
import pytest


def test_add():
    assert calc.add(7, 3) == 10


def test_add_strings():
    assert calc.add("Hello ", "World") == "Hello World"


def test_add_float():
    assert calc.add(12.5, 12.5) == 25
