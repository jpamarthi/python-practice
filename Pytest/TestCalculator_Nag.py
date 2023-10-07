import pytest
from CalculatorApp.Calculater_Nag import *


def test_subtract_numbers(self):
    assert subtract_numbers(8, 6) == 2


def test_add_numbers(self):
    assert add_numbers(2, 3) == 5
    assert add_numbers(5, 7) == 12


def test_divide_numbers(self):
    assert divide_numbers(4, 2) == 2
    assert divide_numbers(10, 2) == 5


def test_multipli_numbers(self):
    assert multipli_numbers(2, 3) == 6
    assert multipli_numbers(5, 6) == 30