import calc
import pytest
import sys


#@pytest.mark.number
#@pytest.mark.skip(reason="do not execute test_add")
@pytest.mark.skipif(sys.version_info > (3, 3), reason="do not execute test_add")
def test_add():
    pass
    assert calc.add(1, 2) == 3
    assert calc.add(2) == 12


@pytest.mark.number
def test_product():
    assert calc.product(2, 3) == 6
    assert calc.product(5, 2) == 10


@pytest.mark.strings
def test_add_string():
    pass
    assert calc.add("Hello", "World") == "Hello World"
    assert type(calc.add("Hello ", "World")) is str
