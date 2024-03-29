import pytest
from Examples.InterviewProblemsApp.InterViewProblemsSaran import find_sum_in_list_approach1, find_sum_in_lst_approach2


def test_find_sum_in_list_approach1():
    assert not find_sum_in_list_approach1([1, 2, 3, 5, 8], 15)
    assert find_sum_in_list_approach1([1, 5, 6, 6, 7], 12)


def test_find_sum_in_lst_approach2():
    assert not find_sum_in_lst_approach2([1, 2, 3, 5, 8], 15)
    assert find_sum_in_lst_approach2([1, 5, 6, 6, 7], 12)