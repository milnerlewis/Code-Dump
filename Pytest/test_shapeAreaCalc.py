import pytest


# Defined functions to test


def circle(radius):
    return 3.14 * (radius ** 2)

def square(side):
    return side ** 2

def rectangle(length, width):
    return length * width

def parollogram(base, height):
    return base * height

def triangle(base, height):
    return 0.5 * base * height


# Testing functions


def test_circle():
    assert circle(5) == 78.5
    assert circle(10) == 314

def test_square():
    assert square(5) == 25
    assert square(10) == 100

def test_rectangle():
    assert rectangle(5, 10) == 50
    assert rectangle(10, 10) == 100

def test_parollogram():
    assert parollogram(5, 10) == 50
    assert parollogram(10, 10) == 100

def test_triangle():
    assert triangle(5, 10) == 25
    assert triangle(10, 10) == 50