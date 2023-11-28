#!/usr/bin/python3
""" this module contains a function that prints a persons's name"""


def say_my_name(first_name, last_name=""):
    """ this function prints out a person's name

    Args:
        first_name (str): first parameter
        last_name (str, optional): last parameter

    Raises:
        TypeError: if first_name or last_name is not a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name != "":
        print("{} {}".format(first_name, last_name))
    else:
        print("{}".format(first_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
