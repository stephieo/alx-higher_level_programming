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
