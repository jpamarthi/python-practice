import pytest
from Examples.MilesAndKilometersApp.ConversionJass import kilometers_to_miles, miles_to_kilometers


def test_kilometers_to_miles():
    assert kilometers_to_miles(4) == 2
    assert kilometers_to_miles(2) == 1


def test_miles_to_kilometers():
    assert miles_to_kilometers(4) == 6
    assert miles_to_kilometers(10) == 16
