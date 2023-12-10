#!/usr/bin/python3
"""test module for `Rectangle` class""""
import unittest
from models.rectangle import Rectangle

class TestRectangleClass(unittest.TestCase):
    """test case for the functionality of the `Rectangle` subclass"""
    """check:
        - id creation
        - privacy of
            -width
            -height
            -x
            -y
        -check that default arguments are working
        -check argument validation of:
            -width
            -height
    """
    