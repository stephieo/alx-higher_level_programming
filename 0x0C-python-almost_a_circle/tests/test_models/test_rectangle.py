#!/usr/bin/python3
"""test module for `Rectangle` class"""
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle

class TestRectangleMethods(unittest.TestCase):
    """tests the simple methods area, display, __str__"""



class TestRectangleInputvalidation(unittest.TestCase):
    """tests the input validation in creation of Rectangle object"""
    """ - seperate tests for each  argument being invalid"""

class TestRectangleArgumentPrivacy(unittest.TestCase):
    """ testing the privacy, getters and setters of arguments"""
class TestRectangleInstantiation(unittest.TestCase):
    """test case for instantiation of the `Rectangle` object"""
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
            -width -x
            -height  -y
        -check return value of area() with all valid inputs
    """
    def setUp(self):
        """set up test objects for TestRectangleClass"""
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10, 0, 0)
        self.r3 = Rectangle(2, 18, 0, 8)
        self.r4 = Rectangle(30, 2, 5, 6, 12)

    def tearDown(self):
        """tear down test objects"""
        del self.r1
        del self.r2
        del self.r3
        del self.r4

    def test_two_args(self):
        """checks the instantiation and input validation of two args to Rectangle"""
        rec1 = Rectangle(20, 1)
        rec2 = Rectangle(2, 10)
        self.assertEqual(rec1.width, 20)
        self.assertEqual(rec2.width, 2)
        self.assertEqual(rec1.id, rec2.id - 1 )

    def test_three_args(self):
        """checks the instantiation and input validation of three args to Rectangle"""
        self.assertEqual(Rectangle(1, 2, 9).x, 9)

    def test_four_args(self):
        """checks the instantiation and input validation of four args to Rectangle"""
        self.assertEqual(Rectangle(1, 2, 9, 10).y, 10)

    def test_five_args(self):
        """checks the instantiation and input validation of five args to Rectangle"""
        self.assertEqual(Rectangle(1, 2, 9, 10, 34).id, 34)


    # def test_id_creation(self):

    #     """checks  id creation with and without arguments"""
    #     self.assertEqual(self.r1.id, 14)
    #     self.assertEqual(self.r2.id, -16)
    #     self.assertEqual(self.r3.id, 15)
    #     self.assertEqual(self.r4.id, 12)


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
        
    def test_area(self):
        """checks the output of area( with various inputs)"""
        self.assertEqual(self.r2.area(), 20)
        self.assertEqual(self.r3.area(), 36)
        self.assertEqual(self.r4.area(), 60)

    def test_display(self):
        """checks that the visual of the rectangle matches its measurements"""
        r2_output = "##\n##\n##\n##\n##\n##\n##\n##\n##\n##\n"
        self.assertEqual(self.r2.display(), r2_output)

        r4_output = "##############################\n##############################\n" 
        self.assertEqual(self.r4.display(), r4_output)

    @patch('builtins.print')
    def test_str_method(self, mock_output):
        """checks that the output of `str()` matches the requirements"""
        r1_str = f"[Rectangle] ({self.r1.id}) {self.r1.x}/{self.r1.y} - {self.r1.width}/{self.r1.height}"
        output_of_str = str(self.r1)
        print(self.r1)
        self.assertEqual(output_of_str, r1_str)
        mock_output.assert_called_once_with(self.r1)

        r3_str = f"[Rectangle] ({self.r3.id}) {self.r3.x}/{self.r3.y} - {self.r3.width}/{self.r3.height}"
        output_of_str = str(self.r3)
        print(self.r3)
        self.assertEqual(output_of_str, r3_str)
        self.assertEqual(output_of_str, r3_str)
        mock_output.assert_called_with(self.r3)

    if __name__ == "__main__":
        unittest.main()