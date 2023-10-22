import pytest
from Examples.MilesAndKilometersApp.ConversionJass import *


def test_kilometers_to_miles():
    assert kilometers_to_miles(2) == 1
    assert kilometers_to_miles(5) == 3


def test_miles_to_kilometers():
    assert miles_to_kilometers(2) == 3
    assert miles_to_kilometers(5) == 8
