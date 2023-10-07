import pytest
from Examples.CalculatorApp.CalculaterNag import *


def test_subtract_numbers():
    assert subtract_numbers(8, 6) == 2


def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(5, 7) == 12


def test_divide_numbers():
    assert divide_numbers(4, 2) == 2
    assert divide_numbers(10, 2) == 5


def test_multipli_numbers():
    assert multipli_numbers(2, 3) == 6
    assert multipli_numbers(5, 6) == 30