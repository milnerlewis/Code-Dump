import pytest


# Defined functions to test


def circle(radius):
    try:
        float(radius)

    except:
        return False
    
    else:
        return 3.14 * (radius ** 2)

def square(side):
    try:
        float(side)

    except:
        return False
    
    else:
        return side ** 2

def rectangle(length, width):
    try:
        float(length)
        float(width)

    except:
        return False
    
    else:
        return length * width

def parollelogram(base, height):
    try:
        float(base)
        float(height)
    
    except:
        return False
    
    else:
        return base * height

def triangle(base, height):
    try:
        float(base)
        float(height)
    
    except:
        return False
    
    else:
        return 0.5 * base * height


# Testing functions


def test_circle():
    assert circle(5) == 78.5
    assert circle(10) == 314
    assert circle(0) == 0
    assert circle("potato") == False

def test_square():
    assert square(5) == 25
    assert square(10) == 100
    assert square(0) == 0
    assert square("potato") == False

def test_rectangle():
    assert rectangle(5, 10) == 50
    assert rectangle(10, 10) == 100
    assert rectangle(1,0) == 0
    assert rectangle("potato", 10) == False

def test_parollelogram():
    assert parollelogram(5, 10) == 50
    assert parollelogram(10, 10) == 100
    assert parollelogram(1,0) == 0
    assert parollelogram("potato", 10) == False

def test_triangle():
    assert triangle(5, 10) == 25
    assert triangle(10, 10) == 50
    assert triangle(1, 0) == 0
    assert triangle("potato", 10) == False