import pytest
from Examples.HelloWorldApp.HelloWorldNag import hello_world


def test_hello_world():
    assert hello_world() == "HelloWorld!"