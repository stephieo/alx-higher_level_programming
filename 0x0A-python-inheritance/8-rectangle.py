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
