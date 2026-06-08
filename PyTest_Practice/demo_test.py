import pytest

@pytest.mark.smoke
def test_sample_one():
    print("Hai")
@pytest.mark.skip    
def test_sample1():
    print("Welcome")
@pytest.mark.regression    
def test_sample2():   
    print("Pytest")
@pytest.mark.skipif(False, reason="Condition is False")
def test_sample3():
    print("World")
@pytest.mark.xfail
def test_sample4():
    assert 1 == 2
@pytest.mark.xfail
def test_sample4():
    assert 1 == 1
@pytest.mark.parametrize("test_input, expected",[(1, 3), (3, 5), (5, 7)])
def test_addition(test_input, expected):
    assert test_input + 2 == expected                  