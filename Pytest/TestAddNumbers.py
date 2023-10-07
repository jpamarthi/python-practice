import pytest
from AdditionApp.AddNumbers_jass import add_numbers


def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(5, 7) == 12