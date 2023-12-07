#!/usr/bin/python3
""" contains class defintion of `Student`"""


class Student:
    """class definition of `Student`"""

    def __init__(self, first_name, last_name, age):
        """initializing `Student` object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dictionary representation of `Student` object"""
        return self.__dict__
