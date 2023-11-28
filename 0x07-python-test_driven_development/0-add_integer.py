#!/usr/bin/python3
""" This is the add_integer module

contains only the add_integer() function

>>>add_integer(4, 5)
9
"""
import doctest


def add_integer(a, b=98):
    """adds two integers or floats

    Args:
        a (int): first number, can be a float too
        b (int, optional): second number, can be a float. Defaults to 98

    Returns:
        sum of the arguments

    Raises:
        TypeError: if inputs are not int or float
    """
    if (type(a) is not int and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and type(b) is not float):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
