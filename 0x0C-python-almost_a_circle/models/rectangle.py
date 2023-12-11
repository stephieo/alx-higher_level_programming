#!/usr/bin/python3
""" module contains class definition for `Rectangle` subclass"""
from models.base import Base


class Rectangle(Base):
    """class definition of `Rectangle` class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """contructor for new instances"""
        super().__init__(id)

        for input in (width, height, x, y):
            if type(input) is not int:
                raise TypeError(f"{input} must be an integer")
        
        for i in (width, height):
            if i <= 0:
                raise ValueError(f"{i} must be > 0")

        for i in (x, y):
            if i < 0:
                raise ValueError(f"{i} must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """getter and setter for `__width`"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """getter and setter for `__height`"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """getter and setter methods for `x`"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """getter and setter methods for `y`"""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    def __del__(self):
        """destructor method for deleted objects"""
        super().__del__