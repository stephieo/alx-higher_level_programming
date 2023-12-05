#!/usr/bin/python3
""" contains the class definition for BaseGeometry"""


class BaseGeometry:
    """class definition of BaseGeometry"""

    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the input for integer_validator"""
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


if __name__ == "__main__":
    import doctest
    doctest.testfile('tests/7-base_geometry.txt')
