import Lesson_10

def test_01():
    assert Lesson_10.plus(2, 2) == 4


def test_02():
    assert Lesson_10.plus(100, 9) == 109, "Неверный результат"


def test_03():
    assert Lesson_10.plus(-1, 1) == 0


def test_zero():
    assert Lesson_10.plus(0, 0) == 0