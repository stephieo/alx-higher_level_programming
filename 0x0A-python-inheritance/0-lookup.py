#!/usr/bin/python3
"""module containing one lookup function"""


def lookup(obj):
    """returns a list of all attributes and methods of an obj"""
    return dir(obj)
