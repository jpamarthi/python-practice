import unittest
from MultiplicationApp.Multipli_saran import multipli_numbers


class MyTestCase(unittest.TestCase):
    def test_multipli_numbers(self):
        assert multipli_numbers(2, 3) == 6
        assert multipli_numbers(5, 6 ) == 30


if __name__ == '__main__':
    unittest.main()
