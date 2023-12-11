#!/usr/bin/python3
"""test module for `Rectangle` class"""
import unittest
from models.rectangle import Rectangle

class TestRectangleClass(unittest.TestCase):
    """test case for the functionality of the `Rectangle` subclass"""
    """check:
        - id creation✅
        -proper output from 0 - 5 arguments, errors for >5 args
        - privacy ,getter and setters of:
            -width✅
            -height✅
            -x✅
            -y✅
        -check that default arguments are working✅
        -check argument validation of:
            -width
            -height
    """
    def setUp(self):
        """set up test objects for TestRectangleClass"""
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10, 0, 0, -16)
        self.r3 = Rectangle(2, 18, 0, 8)
        self.r4 = Rectangle(10, 2, 5, 6, 12)

    def tearDown(self):
        """tear down test objects"""
        del self.r1
        del self.r2
        del self.r3
        del self.r4

    def test_id_creation(self):

        """checks  id creation with and without arguments"""
        self.assertEqual(self.r1.id, 2)
        self.assertEqual(self.r2.id, -16)
        self.assertEqual(self.r3.id, 3)
        self.assertEqual(self.r4.id, 12)

    def test_width_privacy(self):
        """checks that width is not publically accessible"""
        with self.assertRaises(AttributeError):
            self.r1.__width
        
    def test_width_getter_setter(self):
        """checks that getter and setter for width work as defined"""
        self.assertEqual(self.r1.width, 10)
        self.r1.width = 32
        self.assertEqual(self.r1.width, 32)

    def test_height_privacy(self):
        """checks that height is not publically accessible"""
        with self.assertRaises(AttributeError):
            self.r2.__height
        
    def test_height_getter_setter(self):
        """checks that getter and setter for height work as defined"""
        self.assertEqual(self.r2.height, 10)
        self.r2.height = 92
        self.assertEqual(self.r2.height, 92)

    def test_x_privacy(self):
        """checks that x is not publically accessible"""
        with self.assertRaises(AttributeError):
            self.r3.__x
        
    def test_x_getter_setter(self):
        """checks that getter and setter for x work as defined"""
        self.assertEqual(self.r3.x, 0)
        self.r3.x = 92
        self.assertEqual(self.r3.x, 92)

    def test_y_privacy(self):
        """checks that y is not publically accessible"""
        with self.assertRaises(AttributeError):
            self.r4.__y
        
    def test_y_getter_setter(self):
        """checks that getter and setter for y work as defined"""
        self.assertEqual(self.r4.y, 6)
        self.r4.y = 92
        self.assertEqual(self.r4.y, 92)

    def test_input_validation(self):
        """check that inputs amust be positive integers"""
        with self.assertRaises(TypeError):
            temp = Rectangle("one", 2, 9, 3)
        with self.assertRaises(TypeError):
            temp = Rectangle(1, 2, (8, 4), 5)
        with self.assertRaises(ValueError):
            temp = Rectangle(19, 4, -4, 8)
        with self.assertRaises(ValueError):
            temp = Rectangle(11, 0, 9, 3)
        

    if __name__ == "__main__":
        unittest.main()