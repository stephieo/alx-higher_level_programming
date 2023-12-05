#!/usr/bin/python3
""" checks if  object is an instance of specified class or its subclass"""


def is_kind_of_class(obj, a_class):
    """ checks if  object is an instance of specified class or its subclass"""
    return isinstance(obj, a_class)
