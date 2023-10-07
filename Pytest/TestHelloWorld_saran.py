import pytest
from HelloWorldApp.HelloWorld_saran import hello_world


def test_hello_world():
    assert hello_world() == "HelloWorld!"