import pytest
from SubtractionApp.SubtractNumbers import subtract_numbers


def test_subtract_numbers():
    assert subtract_numbers(8, 6) == 2
