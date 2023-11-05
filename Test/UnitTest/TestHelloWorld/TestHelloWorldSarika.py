import unittest
from Examples.HelloWorldApp.HelloWorldSarika import hello_world


class MyTestCase(unittest.TestCase):
    def test_hello_world(self):
        assert hello_world() == "HelloWorld!!!"


if __name__ == '__main__':
    unittest.main()
