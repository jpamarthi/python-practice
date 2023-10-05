import unittest
from AdditionApp.AddNumbers_jass import add_numbers


class MyTestCase(unittest.TestCase):
    def test_add_numbers(self):
        assert add_numbers(2, 3) == 5
        assert add_numbers(5, 7) == 12


if __name__ == '__main__':
    unittest.main()
