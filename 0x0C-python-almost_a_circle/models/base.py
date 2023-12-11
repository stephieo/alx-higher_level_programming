#!/usr/bin/python3
"""this module contains the base class of all other classes in this project"""


class Base:
    """class definition of `Base`"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def __del__(self):
        Base.__nb_objects -= 1