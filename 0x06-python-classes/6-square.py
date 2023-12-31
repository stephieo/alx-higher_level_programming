#!/usr/bin/python3
"""Defines a Square"""


class Square:
    """class definition of Square"""

    def __init__(self, squaresize=0, position=(0, 0)):
        """initializes instances of Square

        Args:
            squaresize(int): length of one side of Square
            position(tuple): coordinates of square object
        """
        if type(squaresize) is not int:
            raise TypeError("size must be an integer")
        if squaresize < 0:
            raise ValueError("size must be >= 0")

        if (not isinstance(position, tuple) or
                not all(isinstance(i, int) for i in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2 or not all(i >= 0 for i in position):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = squaresize
        self.__position = position

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

    @property
    def position(self):
        """tuple: returns cordinates of square"""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple)
                or not all(isinstance(i, int) for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2 or not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculates area of square"""
        return self.__size * self.__size

    def my_print(self):
        """prints a visual representation of a Square object"""
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                print("" * self.__position[1])

            for i in range(self.__size):
                if self.__position[0] > 0:
                    print("{}".format("_" * self.__position[0]), end="")
                print("{}".format('#' * self.__size))
