import pytest
from Examples.FindLargestSmallestNumberApp.FindLargestNumberSarika import find_largest_two_numbers, \
    find_largest_three_numbers, find_smallest_two_numbers, find_smallest_three_numbers


def test_find_largest_two_numbers():
    assert find_largest_two_numbers(200, 400) == 400
    assert find_largest_two_numbers(800, 500) == 800


def test_find_largest_three_numbers():
    assert find_largest_three_numbers(100, 200, 400) == 400
    assert find_largest_three_numbers(800, 100, 200) == 800
    assert find_largest_three_numbers(100, 700, 200) == 700


def test_find_smallest_two_numbers():
    assert find_smallest_two_numbers(200, 100) == 100
    assert find_smallest_two_numbers(300, 500) == 300


def test_find_smallest_three_numbers():
    assert find_smallest_three_numbers(100, 200, 400) == 100
    assert find_smallest_three_numbers(800, 100, 200) == 100
    assert find_smallest_three_numbers(200, 700, 100) == 100

