#!/usr/bin/python3
"""Defines a Square"""


class Square:
    """class definition of Square"""

    def __init__(self, squaresize=0):
        """initializes instances of Square

        Args:
            squaresize(int): length of one side of Square
        """
        if type(squaresize) is not int:
            raise TypeError("size must be an integer")
        if squaresize < 0:
            raise ValueError("size must be >= 0")
        self.__size = squaresize

    @property
    def size(self):
        """int: size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculates area of square"""
        return self.__size * self.__size

    def my_print(self):
        """prints a visual representation of a Square object"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("{}".format('#' * self.__size))
