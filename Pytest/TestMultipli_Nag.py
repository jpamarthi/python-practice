import pytest
from MultiplicationApp.Multipli_saran import multipli_numbers


def test_multipli_numbers():
    assert multipli_numbers(2, 3) == 6
    assert multipli_numbers(5, 6) == 30
