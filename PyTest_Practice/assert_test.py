import pytest

def test_simple_assertion():
    assert 1 + 1 == 2
def test_perfect_assertion():
    assert 2 == 2
def test_wrong_assertion():
    assert 1 == 2
def test_equal_assertion():
    x = 1
    y = 1
    assert x == y
def test_not_equal_assertion():
    x = 5
    y = 10
    assert x != y
def test_in_assertion():
    x = 1
    y = [1,2,3]
    assert x in y   
def test_Not_in_assertion():
    x = 1
    y = [1,2,3]
    assert x not in y             