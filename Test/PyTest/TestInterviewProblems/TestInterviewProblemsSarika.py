import pytest
from Examples.InterviewProblemsApp.InterviewProblemsSarika import find_sum_in_list_approach1, \
    find_sum_in_list_approach3, find_sum_in_list_approach4


def test_find_sum_in_list_approach1():
    assert not find_sum_in_list_approach1([1, 2, 3, 4, 9], 8)
    assert find_sum_in_list_approach1([3, 4, 5, 6, 9], 11)
    assert find_sum_in_list_approach1([1, 4, 2, 5, 3, 8], 7)


def test_find_sum_in_list_approach3():
    assert not find_sum_in_list_approach3([1, 2, 3, 4, 9], 8)
    assert find_sum_in_list_approach3([3, 4, 5, 6, 9], 11)
    assert find_sum_in_list_approach3([1, 4, 2, 5, 3, 8], 7)


def test_find_sum_in_list_approach4():
    assert not find_sum_in_list_approach4([1, 2, 3, 4, 9], 8)
    assert find_sum_in_list_approach4([3, 4, 5, 6, 9], 11)
    assert find_sum_in_list_approach4([1, 4, 2, 5, 3, 8], 7)
