#!/usr/bin/python3
"""defines the subclass `Rectangle`"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """defines the subclass `Rectangle`"""
    def __init__(self, width, height):
        """initiallize object"""
        super().integer_validator("Rectangle", width)
        super().integer_validator("Rectangle", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
