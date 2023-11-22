import pytest
from Examples.SortingApp.SortingNag import sorting_list_bubble_sort


def test_sorting_list_bubble_sort():
    assert sorting_list_bubble_sort([10, 3, 4, 2, 1]) == [1, 2, 3, 4, 10]
