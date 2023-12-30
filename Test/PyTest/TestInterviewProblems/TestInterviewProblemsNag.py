import pytest
from Examples.InterviewProblemsApp.InterviewProblemsNag import find_sum_in_list, find_sum_in_list_3


def test_find_sum_in_list():
    assert not find_sum_in_list([1, 3, 4, 9], 8)
    assert find_sum_in_list([3, 5, 6, 9], 11)
    assert find_sum_in_list([4, 2, 5, 3, 8], 7)


def test_find_sum_in_list_3():
    assert not find_sum_in_list_3([1, 3, 4, 9], 8)
    assert find_sum_in_list_3([3, 5, 6, 9], 11)
    assert find_sum_in_list_3([4, 2, 5, 3, 8], 7)
