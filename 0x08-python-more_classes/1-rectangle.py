#!/usr/bin/python3
""" module defining the class Rectangle"""


class Rectangle:
    """class definition of Rectangle"""
    def __init__(self, width=0, height=0):
        """initializes instances of Rectangle

        Args:
            width (int, optional): length of the rectangle
            height (int, optional): height of the rectangle
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

        @property
        def width(self):
            """getter method for private '__width' property"""
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """getter method for private '__height' property"""
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
