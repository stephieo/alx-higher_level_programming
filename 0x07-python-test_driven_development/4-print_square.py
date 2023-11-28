#!/usr/bin/python3
""" this contains a function print_square"""


def print_square(size):
    """ this function prints out a square of the given size

    Args:
        size (int): length of one side of the square

    Raises:
        TypeError: if size is not an integer or is a negative float
        ValueError: if size is less than 0
    """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(int(size)):
        print("#" * int(size))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
