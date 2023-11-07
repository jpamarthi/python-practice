import pytest
from Examples.FindLargestSmallestNumberApp.FindLargestNumberNag import find_largest_two_numbers


def test_find_largest_two_numbers():
    assert find_largest_two_numbers(100, 200) == 200
    assert find_largest_two_numbers(300, 200) == 300
