import pytest

def add(x,y):
    return x + y

def test_add():
    assert add(2,3) == 5
    assert add(1,2) == 3
    assert add(1,1) == 2