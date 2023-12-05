#!/usr/bin/python3
""" contains the class definition for BaseGeometry"""


class BaseGeometry:
    """class definition of BaseGeometry"""
    def area(self):
        raise Exception("area() is not implemented")

    def intege_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
