import pytest
from HelloWorldApp.HelloWorld_Nagaraju import hello_world


def test_hello_world():
    assert hello_world() == "HelloWorld!"