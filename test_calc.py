import calc
import pytest


@pytest.mark.parametrize('num1, num2, output',[
    (7, 3, 10),
    ("Hello ", "World", "Hello World"),
    (12.5, 12.5, 25)
])
def test_add(num1, num2, output):
    assert calc.add(num1, num2) == output
