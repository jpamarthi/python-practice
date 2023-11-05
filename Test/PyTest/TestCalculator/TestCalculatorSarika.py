import pytest
from Examples.CalculatorApp.CalculatorSarika import add_numbers, subtract_numbers, divide_numbers, multipli_numbers, \
    exponentiation_number


def test_add_numbers():
    assert add_numbers(2, 4) == 6
    assert add_numbers(5, 2) == 7
    assert add_numbers(5, 4) == 9


def test_subtract_numbers():
    assert subtract_numbers(2, 1) == 1


def test_divide_numbers():
    assert divide_numbers(2, 2) == 1
    assert divide_numbers(8, 2) == 4


def test_multipli_numbers():
    assert multipli_numbers(2, 2) == 4
    assert multipli_numbers(2, 6) == 12


def test_exponentiation_numbers():
    assert exponentiation_number(2, 2) == 4
    assert exponentiation_number(2, 1) == 2
