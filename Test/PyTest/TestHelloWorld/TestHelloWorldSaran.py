import pytest
from Examples.HelloWorldApp.HelloWorldSaran import hello_world


def test_hello_world():
    assert hello_world() == "HelloWorld!"