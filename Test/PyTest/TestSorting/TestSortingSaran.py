import pytest
from Examples.SortingApp.SortingSaran import sorting_list_bubble_sort


def test_sorting_list_bubble_sort():
    assert sorting_list_bubble_sort([3, 6, 5, 2, 1]) == [1, 2, 3, 5, 6]
