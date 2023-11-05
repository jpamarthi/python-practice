import unittest
from Examples.CalculatorApp.CalculatorJass import add_numbers, subtract_numbers, divide_numbers, multipli_numbers, exponentiation_number


class MyTestCase(unittest.TestCase):
    def test_add_numbers(self):
        assert add_numbers(2, 3) == 5
        assert add_numbers(5, 7) == 12

    def test_subtract_numbers(self):
        assert subtract_numbers(8, 6) == 2

    def test_divide_numbers(self):
        assert divide_numbers(4, 2) == 2
        assert divide_numbers(10, 2) == 5

    def test_multipli_numbers(self):
        assert multipli_numbers(2, 3) == 6
        assert multipli_numbers(5, 6 ) == 30

    def test_exponentiation_numbers(self):
        assert exponentiation_number(2, 3) == 8
        assert exponentiation_number(3, 3) == 27


if __name__ == '__main__':
    unittest.main()
