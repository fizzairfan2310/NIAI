from calculator import add, subtratct


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtratct(5, 3) == 2
    assert subtratct(1, 1) == 0
    assert subtratct(0, 0) == 0