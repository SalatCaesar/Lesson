import sys
import pytest
import L_1
from datetime import datetime

@pytest.mark.skip('Нафиг')
def test_01():
    assert L_1.plus(2, 2) == 4

def test_02():
    assert L_1.plus(100, 9) == 108, "Неверный результат"

def test_03():
    date = datetime.today().strftime("%d.%m")
    if date == '27.12':
        pytest.skip('Not today, mazafaka')
    assert L_1.plus(-1, 1) == 0


@pytest.mark.skipif(sys.platform == 'win32', reason='Tvoi soft govno')
def test_zero():
    assert L_1.plus(0, 0) == 0