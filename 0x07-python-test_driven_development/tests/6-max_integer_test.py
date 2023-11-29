#!/usr/bin/python3
""" unittest module for max_integer"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ this class is a test case for the function 'max_integer'"""

    """empty list
     one value in list
     2 values in list
     element not an integer
     negative values
      values include 0 : positive and negative
      duplicate values  not max
      duplicate values max
      all values are the same
      positive and negative integers
      """

      def test_empty_list(self):
        """testing empty lists"""
        self.assertEqual(max_integer(), None)