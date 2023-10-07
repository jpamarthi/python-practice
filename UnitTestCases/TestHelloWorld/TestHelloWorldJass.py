import unittest
from HelloWorldApp.HelloWorld_Jass import hello_world


class MyTestCase(unittest.TestCase):
    def test_hello_world(self):
        assert hello_world("Hello World!") == "Hello World!"


if __name__ == '__main__':
    unittest.main()
