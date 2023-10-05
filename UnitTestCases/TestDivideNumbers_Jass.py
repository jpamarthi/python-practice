import unittest
from DivisionApp.DivideNumbers_Jass import divide_numbers

class MyTestCase(unittest.TestCase):

    def test_divide_numbers(self):
        assert divide_numbers(4, 2) == 2
        assert divide_numbers(10, 2) == 5


if __name__ == '__main__':
    unittest.main()
