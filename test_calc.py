import calc


def test_add():
    pass
    assert calc.add(1, 2) == 3
    assert calc.add(2) == 12


def test_product():
    assert calc.product(2, 3) == 6
    assert calc.product(5, 2) == 10
