#!/usr/bin/python3
""" module defining the class Rectangle"""


class Rectangle:
    """class definition of Rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initializes instances of Rectangle

        Args:
            width (int, optional): length of the rectangle
            height (int, optional): height of the rectangle
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter method for private '__width' property"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
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
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the Rectangle object"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the Rectangle object"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """defines the visual representation of Rectangle object"""
        if self.__width == 0 or self.height == 0:
            return ""
        display = ""
        for i in range(self.__height):
            if i != self.__height - 1:
                display += "{}\n".format("#" * self.__width)
            else:
                display += "{}".format("#" * self.__width)
        return display

    def __repr__(self):
        """returns a string representation that can reproduce the object"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
