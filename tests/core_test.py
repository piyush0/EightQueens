from core import runner


def test_one():
    assert runner(1) == 1


def test_four():
    assert runner(4) == 2


def test_six():
    assert runner(6) == 4


def test_eight():
    assert runner(8) == 92
