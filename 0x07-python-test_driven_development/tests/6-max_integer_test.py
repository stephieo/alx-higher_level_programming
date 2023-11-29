#!/usr/bin/python3
""" unittest module for max_integer"""
max_integer = __import__('6-max_integer').max_integer
import unittest



class TestMaxInteger(unittest.TestCase):
    """ this class is a test case for the function 'max_integer'"""

    """✅empty list
     ✅one value in list(pos, neg, 0)
     ✅2 values in list(pos, neg, middle)
     ✅element not an integer (float, tuple, string)
     negative values
      values include 0 : positive and negative
     ✅ duplicate values  not max
      ✅ values max
      ✅all values are the same
      positive and negative 
      ✅max at beginning
      ✅max at end
      ✅max in the middle
      """

    def test_empty(self):
      """testing no argument and empty list"""
      self.assertEqual(max_integer(), None)

      mylist = []
      self.assertEqual(max_integer(mylist), None)

    def test_one_value(self):
      """test list with one value"""
      mylist = [8]
      self.assertEqual(max_integer(mylist), 8)

      mylist = [0]
      self.assertEqual(max_integer(mylist), 0)

      mylist = [-4]
      self.assertEqual(max_integer(mylist), -4)
    
    def test_two_values(self):
      """test lists with 2 values"""
      mylist = [8, 4]
      self.assertEqual(max_integer(mylist), 8)

      mylist =  [0, 0]
      self.assertEqual(max_integer(mylist), 0)

      mylist = [-2, -8]
      self.assertEqual(max_integer(mylist), -2)

    def test_not_integer(self):
      """test lists with non-integer values"""

      mylist = ["good", "hello", "play", "work"]
      self.assertEqual(max_integer(mylist), "work")

      mylist = [8.9, 3.5, 0.4, 2.55]
      self.assertEqual(max_integer(mylist), 8.9)

      mylist = [(2,3), (9, 19), (5,6)]
      self.assertEqual(max_integer(mylist), (9, 19))

    def test_max_location(self):
      """test list with the max at different points"""
      mylist = [29, 4, 2, 9]
      self.assertEqual(max_integer(mylist), 29)

      mylist = [4, 9 ,29, 5, 2]
      self.assertEqual(max_integer(mylist), 29)

      mylist = [2, 9, 5, 4, 29]
      self.assertEqual(max_integer(mylist), 29)

    def test_duplicates(self):
      """ tests lists with duplicates"""
      mylist = [8, 8, 2, 7, 32]
      self.assertEqual(max_integer(mylist), 32)

      mylist = [8, 1, 2, 32, 32, 4]
      self.assertEqual(max_integer(mylist), 32)

      mylist = [32, 32, 32, 32, 32, 32]
      self.assertEqual(max_integer(mylist), 32)

    def test_mixed_sign(self):
      """lists with both positive and negative values"""
      mylist = [-4, 6, -9, 0, -12]
      self.assertEqual(max_integer(mylist), 6)

      mylist = [-4, -6, -9, 0, -12]
      self.assertEqual(max_integer(mylist), 0)

      mylist = [-4, -6, -9, -10, -12]
      self.assertEqual(max_integer(mylist), -4)

if __name__ == "__main__":
  unittest.main()
