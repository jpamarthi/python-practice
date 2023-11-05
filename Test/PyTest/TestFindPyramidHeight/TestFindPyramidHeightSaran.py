import pytest
from Examples.FindPyramidHeightApp.FindPyramidHeightSaran import find_pyramid_height


def test_find_pyramid_height():
    assert find_pyramid_height(6) == 3
    assert find_pyramid_height(20) == 5
    assert find_pyramid_height(1000) == 44
    assert find_pyramid_height(2) == 1
    assert find_pyramid_height(1) == 1
    assert find_pyramid_height(0) == 0
    assert find_pyramid_height(-1) == 0
    assert find_pyramid_height(-1000) == 0
    assert find_pyramid_height(1001) == 44

