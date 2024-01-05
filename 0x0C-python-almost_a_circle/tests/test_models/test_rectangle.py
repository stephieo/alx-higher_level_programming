#!/usr/bin/python3
"""test module for `Rectangle` class"""
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
import sys

class TestRectangleMethods(unittest.TestCase):
    """tests the  methods area, display, __str__ and update"""

    def setUp(self):
        """set up test objects for TestRectangleMethods"""
        self.A = Rectangle(20, 3)
        self.B = Rectangle(2, 10, 1, 1)
        self.C = Rectangle(3, 19, 1, 9)
        self.D = Rectangle(30, 2, 6, 7, 13)

    def tearDown(self):
        """tear down test objects"""
        del self.A
        del self.B
        del self.C
        del self.D

    def test_area(self):
        """checks the output of area( with various inputs)"""
        self.assertEqual(self.B.area(), 20)
        self.assertEqual(self.C.area(), 57)
        self.assertEqual(self.D.area(), 60)
    
    def test_display(self):
        """checks that the visual of the rectangle matches its measurements"""
        
        captured_output = StringIO()
        sys.stdout = captured_output
        self.B.display()
        sys.stdout = sys.__stdout__
        expected = "\n ##\n ##\n ##\n ##\n ##\n ##\n ##\n ##\n ##\n ##\n" 
        self.assertEqual(expected, captured_output.getvalue())

        r1 = Rectangle(2, 3, 2, 2)
        captured_output = StringIO()
        sys.stdout = captured_output
        r1.display()
        sys.stdout = sys.__stdout__  
        expected = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(captured_output.getvalue(), expected)

    @patch('builtins.print')
    def test_str_method(self, mock_output):
        """checks that the output of `str()` matches the requirements"""
        A_str = f"[Rectangle] ({self.A.id}) {self.A.x}/{self.A.y} - {self.A.width}/{self.A.height}"
        output_of_str = str(self.A)
        print(self.A)
        self.assertEqual(output_of_str, A_str)
        mock_output.assert_called_once_with(self.A)

        C_str = f"[Rectangle] ({self.C.id}) {self.C.x}/{self.C.y} - {self.C.width}/{self.C.height}"
        output_of_str = str(self.C)
        print(self.C)
        self.assertEqual(output_of_str, C_str)
        self.assertEqual(output_of_str, C_str)
        mock_output.assert_called_with(self.C)

    def test_update_args(self):
        """test funtionality of update method using args only"""
        old_id = self.B.id
        self.B.update()
        self.assertEqual(self.B.id, old_id)

        self.B.update(77)
        self.assertEqual(self.B.id, 77)

        self.A.update(30, 5)
        self.assertEqual(self.A.id, 30)
        self.assertEqual(self.A.width, 5)

        self.C.update(22, 4, 8)
        self.assertEqual(self.C.id, 22)
        self.assertEqual(self.C.width, 4)
        self.assertEqual(self.C.height, 8)

        self.D.update(21, 6, 4, 2, 4)
        self.assertEqual(self.D.id, 21)
        self.assertEqual(self.D.x, 2)
        self.assertEqual(self.D.y, 4)
        
    def test_update_kwargs(self):
        """testing update method  with kwargs and args"""
        self.C.update(id=39)
        self.assertEqual(self.C.id, 39)
        self.C.update(id=19, width=9)
        self.assertEqual(self.C.width, 9)
        self.C.update(id=39, width=3, height=2)
        self.assertEqual(self.C.height, 2)
        self.C.update(id=39, width=1, height=4, x=4)
        self.assertEqual(self.C.x, 4)
        self.C.update(id=39, width=8, height=17, x=9, y=6)
        self.assertEqual(self.C.y, 6)

class TestRectangleJsonMethods(unittest.TestCase):
    """test the methods concerned with serialization and deserialization"""
    def test_to_dictionary(self):
        """checks that the dictionary format returned by `to_dictionary` 
        contains 5 keys: id, width, height, x, y
        """
        try1 = Rectangle(4, 5, 9, 2, 23)
        self.assertIn("x", try1.to_dictionary().keys())
        self.assertIn("y", try1.to_dictionary().keys())
        self.assertIn("width", try1.to_dictionary().keys())
        self.assertIn("height", try1.to_dictionary().keys())
        self.assertIn("id", try1.to_dictionary().keys())

class TestRectangleInputvalidation(unittest.TestCase):
    """tests the input validation in creation of Rectangle object"""
    def test_input_validation_type(self):
        """check that each input (arguments 1 - 5) must be positive integers """
        with self.assertRaises(TypeError):
            temp = Rectangle("one", 2, 9, 3)
        with self.assertRaises(TypeError):
            temp = Rectangle(1, "2", 9, 5)
        with self.assertRaises(TypeError):
            temp = Rectangle(1, 2, "9", 5)
        with self.assertRaises(TypeError):
            temp = Rectangle(1, 2, 9, "5")

    def test_input_validation_value(self):
        with self.assertRaises(ValueError):
            temp = Rectangle(-2, 4)
        with self.assertRaises(ValueError):
            temp = Rectangle(2, -4)
        with self.assertRaises(ValueError):
            temp = Rectangle(0, 5)
        with self.assertRaises(ValueError):
            temp = Rectangle(5, 0)
        with self.assertRaises(ValueError):
            temp = Rectangle(19, 4, -4, 8)
        with self.assertRaises(ValueError):
            temp = Rectangle(11, 7, 9, -3)

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
        self.assertEqual(Rectangle(12, 12, 3).x, 3)
        self.assertEqual(Rectangle(1, 2, 9).x, 9)

    def test_four_args(self):
        """checks the instantiation and input validation of four args to Rectangle"""
        self.assertEqual(Rectangle(2, 4, 18, 20).y, 20)
        self.assertEqual(Rectangle(1, 2, 9, 10).y, 10)

    def test_five_args(self):
        """checks the instantiation and input validation of five args to Rectangle"""
        self.assertEqual(Rectangle(2, 4, 18, 20, 68).id, 68)
        self.assertEqual(Rectangle(1, 2, 9, 10, 34).id, 34)


    def test_id_creation(self):

        """checks  id creation with and without arguments"""
        self.assertEqual(self.r2.id, self.r1.id + 1)
        self.assertEqual(self.r3.id, self.r2.id + 1)
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

          

    if __name__ == "__main__":
        unittest.main()