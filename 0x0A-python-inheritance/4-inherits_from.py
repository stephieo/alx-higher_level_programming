#!/usr/bin/python3
"""checks if class of object is a subclass of specified class"""


def inherits_from(obj, a_class):
    """checks if class of object is a subclass of specified class"""
    return issubclass(type(obj), a_class)
