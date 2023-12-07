#!/usr/bin/python3
""" contains class defintion of `Student`"""


class Student:
    """class definition of `Student`"""

    def __init__(self, first_name, last_name, age):
        """initializing `Student` object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns dictionary representation of `Student` object"""

        if (type(attrs) is list and
                all(isinstance(attr, str) for attr in attrs)):
            new_dict = {attr: getattr(self, attr) for attr in attrs
                        if hasattr(self, attr)}
            return new_dict

        return self.__dict__
