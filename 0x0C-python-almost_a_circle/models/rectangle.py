#!/usr/bin/python3
""" module contains class definition for `Rectangle` subclass"""
from models.base import Base


class Rectangle(Base):
    """class definition of `Rectangle` class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """contructor for new instances
        Args:
            width (int): length of rectangle
            height (int): breadth of rectangle
            x (int): location of rectangle on x axis
            y (int): location of rectangle on y axis
        """
        super().__init__(id)

        for index, value in enumerate((width, height)):
            if type(value) is not int:
                raise TypeError(
                    f"{'width' if index == 0 else 'height'}"
                    f" must be an integer"
                )

        for index, value in enumerate((x, y)):
            if type(value) is not int:
                raise TypeError(
                    f"{'x' if index == 0 else 'y'} "
                    f"must be an integer"
                )

        for index, value in enumerate((width, height)):
            if value <= 0:
                raise ValueError(
                    f"{'width' if index == 0 else 'height'} "
                    f"must be > 0"
                )

        for index, value in enumerate((x, y)):
            if value < 0:
                raise ValueError(
                    f"{'x' if index == 0 else 'y'} "
                    f"must be >= 0"
                )

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
        if type(value) is not int:
            raise TypeError(f"width must be an integer")
        if value <= 0:
            raise ValueError(f"width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter and setter for `__height`"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError(f"height must be an integer")
        if value <= 0:
            raise ValueError(f"height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter and setter methods for `x`"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError(f"x must be an integer")
        if value < 0:
            raise ValueError(f"x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter and setter methods for `y`"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError(f"y must be an integer")
        if value < 0:
            raise ValueError(f"y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of a rectangle object"""
        return (self.__width * self.__height)

    def display(self):
        """prints out a visual of a rectangle object"""
        image = ""
        for x in range(self.__height):
            image += f"{'#' * self.__width}\n"
        return image

    def __str__(self):
        """prints out a string representation of a Rectangle object"""
        return (
            f"[Rectangle] ({self.id}) "
            f"{self.x}/{self.y} - {self.width}/{self.height}"
        )

    def __del__(self):
        """destructor method for deleted objects"""
        super().__del__
