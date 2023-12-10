#!/usr/bin/python3
""" module contains class definition for `Rectangle` subclass"""
from base import Base


class Rectangle(Base):
    """class definition of `Rectangle` class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """contructor for new instances"""
        super().__init__(id)
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
        return self.___x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """getter and setter methods for `y`"""
        return self.___y

    @y.setter
    def y(self, value):
        self.__y = value



r1 = Rectangle(10, 2)
print(r1.id)

r2 = Rectangle(2, 10)
print(r2.id)

r3 = Rectangle(10, 2, 0, 0, 12)
print(r3.id)