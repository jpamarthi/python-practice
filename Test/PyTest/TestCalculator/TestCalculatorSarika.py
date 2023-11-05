import pytest
from Examples.CalculatorApp.CalculatorSarika import add_numbers, subtract_numbers, divide_numbers, multipli_numbers, \
    exponentiation_number


def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(5, 7) == 12
    assert add_numbers(5, 4) == 9


def test_subtract_numbers():
    assert subtract_numbers(8, 6) == 2


def test_divide_numbers():
    assert divide_numbers(4, 2) == 2
    assert divide_numbers(10, 2) == 5


def test_multipli_numbers():
    assert multipli_numbers(2, 3) == 6
    assert multipli_numbers(5, 6) == 30


def test_exponentiation_numbers():
    assert exponentiation_number(2, 3) == 8
    assert exponentiation_number(3, 3) == 27
