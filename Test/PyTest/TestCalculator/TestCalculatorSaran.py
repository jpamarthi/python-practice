import pytest
from Examples.CalculatorApp.calculatorSaran import add_numbers,divide_numbers,subtract_numbers,modulo_numbers,multipli_numbers,find_odd_even


def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(5, 7) == 12


def test_divide_numbers():
    assert divide_numbers(4, 2) == 2
    assert divide_numbers(10, 2) == 5


def test_multipli_numbers():
    assert multipli_numbers(2, 3) == 6
    assert multipli_numbers(5, 6) == 30


def test_subtract_numbers():
    assert subtract_numbers(8, 6) == 2


def test_modulo_numbers():
    assert modulo_numbers(4, 2) == 0


def test_find_odd_even():
    assert find_odd_even(1) == "Odd"
    assert find_odd_even(2) == "Even"
