#!/usr/bin/python3
"""module containin class definition of the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class definition of subclass `Square`"""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor for instances of `Square`
        Args:
            size (int): length of one size
            x (int): location of rectangle on x axis
            y (int): location of rectangle on y axis
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter and setter for size, which is with in Rectangle class"""
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError(f"width must be an integer")
        if value <= 0:
            raise ValueError(f"width must be > 0")
        self.width = value

    def update(self, *args, **kwargs):
        """updates attributes of square object"""
        i = 0
        if args and len(args) != 0:
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
                i += 1
        elif len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """prints out a string representation of a Square object"""
        return (
            f"[Square] ({self.id}) "
            f"{self.x}/{self.y} - {self.width}"
        )

    def to_dictionary(self):
        """returns the dictionary representation of a square"""

        sq_dict = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
