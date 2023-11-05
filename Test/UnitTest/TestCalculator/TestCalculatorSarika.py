import unittest
from Examples.CalculatorApp.CalculatorSarika import add_numbers, subtract_numbers, divide_numbers, multipli_numbers, \
    exponentiation_number


class MyTestCase(unittest.TestCase):
    def test_add_numbers(self):
        assert add_numbers(2, 2) == 4
        assert add_numbers(5, 2) == 7

    def test_subtract_numbers(self):
        assert subtract_numbers(8, 7) == 1

    def test_divide_numbers(self):
        assert divide_numbers(6, 2) == 3
        assert divide_numbers(10, 5) == 2

    def test_multipli_numbers(self):
        assert multipli_numbers(2, 4) == 8
        assert multipli_numbers(5, 7) == 35

    def test_exponentiation_numbers(self):
        assert exponentiation_number(4, 2) == 16
        assert exponentiation_number(3, 2) == 9


if __name__ == '__main__':
    unittest.main()
