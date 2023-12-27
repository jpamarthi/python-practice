import pytest
from Examples.InterviewProblemsApp.InterviewProblemsJass import find_sum_in_list


def test_find_sum_in_list():
    assert not find_sum_in_list([1, 2, 4, 9], 7)
    assert find_sum_in_list([1, 2, 4, 8], 10)
