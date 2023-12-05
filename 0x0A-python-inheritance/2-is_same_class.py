#!/usr/bin/python3
"""checks if object is exactly an instance of specified class"""


def is_same_class(obj, a_class):
    """checks if object is exactly an instance of specified class"""
    return type(obj) is a_class
