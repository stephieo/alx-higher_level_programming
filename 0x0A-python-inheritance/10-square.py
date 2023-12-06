#!/usr/bin/python3
""" defines subclass of `Rectangle`, `Square`"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """definition of the subclass `Square`"""
    def __init__(self, size):
        """instantiation of square object"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """defines area of a square"""
        return self.__size ** 2
