import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.main import Calculator


def test_add():
    calc = Calculator()
    assert calc.add(3, 5) == 8


def test_add_negative():
    calc = Calculator()
    assert calc.add(-1, -1) == -2
