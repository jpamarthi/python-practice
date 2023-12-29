import pytest
from Examples.InterviewProblemsApp.InterViewProblemsSaran import find_sum_in_list, find_sum_in_lst_approach2


def test_find_sum_in_list():
    assert not find_sum_in_list([5, 3, 4, 8], 6)
    assert find_sum_in_list([1, 2, 5, 10], 12)


def test_find_sum_in_lst_approach2():
    assert not find_sum_in_lst_approach2([5, 3, 4, 8], 6)
    assert find_sum_in_lst_approach2([1, 2, 5, 10], 12)