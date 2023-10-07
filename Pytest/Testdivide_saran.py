import pytest
from DivisionApp.DivideNumbers_Jass import divide_numbers


def test_divide_numbers():
    assert divide_numbers(4, 2) == 2
    assert divide_numbers(10, 2) == 5
