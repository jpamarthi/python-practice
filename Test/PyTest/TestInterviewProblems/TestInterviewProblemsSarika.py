import pytest
from Examples.InterviewProblemsApp.InterviewProblemsSarika import find_sum_in_list, find_sum_in_list_3, find_sum_in_list_4


def test_find_sum_in_list():
    assert not find_sum_in_list([1, 2, 3, 4, 9], 8)
    assert find_sum_in_list([3, 4, 5, 6, 9], 11)
    assert find_sum_in_list([1, 4, 2, 5, 3, 8], 7)


def test_find_sum_in_list_3():
    assert not find_sum_in_list_3([1, 2, 3, 4, 9], 8)
    assert find_sum_in_list_3([3, 4, 5, 6, 9], 11)
    assert find_sum_in_list_3([1, 4, 2, 5, 3, 8], 7)


def test_find_sum_in_list_4():
    assert not find_sum_in_list_3([1, 2, 3, 4, 9], 8)
    assert find_sum_in_list_3([3, 4, 5, 6, 9], 11)
    assert find_sum_in_list_3([1, 4, 2, 5, 3, 8], 7)
