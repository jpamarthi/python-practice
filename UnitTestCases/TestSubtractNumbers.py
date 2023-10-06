import unittest
from SubtractionApp.SubtractNumbers import subtract_numbers


class MyTestCase(unittest.TestCase):
    def test_subtract_numbers(self):
        assert subtract_numbers(8, 6) == 2


if __name__ == '__main__':
    unittest.main()
