import pytest
from Examples.InterviewProblemsApp.InterviewProblemsJass import find_sum_in_list, find_sum_in_lst_approach2


def test_find_sum_in_list():
    assert not find_sum_in_list([1, 2, 4, 9], 7)
    assert find_sum_in_list([1, 2, 4, 8], 10)


def test_find_sum_in_lst_approach2():
    assert not find_sum_in_lst_approach2([1, 2, 4, 9], 7)
    assert find_sum_in_lst_approach2([1, 2, 4, 8], 10)