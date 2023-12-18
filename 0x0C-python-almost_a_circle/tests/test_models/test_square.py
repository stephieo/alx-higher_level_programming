#!/usr/bin/python3
""" unittest file for `Square` class"""
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquareInstantiation(unittest.TestCase):
    """"