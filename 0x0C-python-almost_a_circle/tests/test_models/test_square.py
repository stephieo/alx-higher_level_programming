#!/usr/bin/python3
""" unittest file for `Square` class"""
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
import sys

class TestSquareInstantiation(unittest.TestCase):
    """" test case for instantiation of Square test case"""
    
    def setUp(self):
        """set up test objects for TestSquareClass"""
        self.s1 = Square(10)
        self.s2 = Square(2, 0, 0)
        self.s3 = Square(2, 0, 8)
        self.s4 = Square(30, 5, 6, 12)

    def tearDown(self):
        """tear down test objects"""
        del self.s1
        del self.s2
        del self.s3
        del self.s4

    def test_two_args(self):
        """checks the instantiation and input validation of two args to Square"""
        sq1 = Square(20, 1)
        sq2 = Square(2, 10)
        self.assertEqual(sq1.width, 20)
        self.assertEqual(sq2.width, 2)
        self.assertEqual(sq1.id, sq2.id - 1 )

    def test_three_args(self):
        """checks the instantiation and input validation of three args to Square"""
        self.assertEqual(Square(12, 12, 3).x, 12)
        self.assertEqual(Square(1, 2, 9).y, 9)

    def test_four_args(self):
        """checks the instantiation and input validation of four args to Square"""
        self.assertEqual(Square(2, 4, 18, 20).id, 20)
        self.assertEqual(Square(1, 2, 9, 10).id, 10)

class TestSquareInputvalidation(unittest.TestCase):
    """tests the input validation in creation of Square object"""
    def test_input_validation_type(self):
        """check that each input (arguments 1 - 4) must be positive integers """
        with self.assertRaises(TypeError):
            temp = Square("one", 2, 9, 3)
        with self.assertRaises(TypeError):
            temp = Square(1, "2", 9, 5)
        with self.assertRaises(TypeError):
            temp = Square(1, 2, "9", 5)

    def test_input_validation_value(self):
        with self.assertRaises(ValueError):
            temp = Square(-2, 4)
        with self.assertRaises(ValueError):
            temp = Square(2, -4)
        with self.assertRaises(ValueError):
            temp = Square(0)
        with self.assertRaises(ValueError):
            temp = Square(19, 4, -4)

class TestSquareMethods(unittest.TestCase):
    """tests the  methods area, display, __str__ and update"""

    def setUp(self):
        """set up test objects for TestSquareMethods"""
        self.A = Square(20)
        self.B = Square(2, 1, 1)
        self.C = Square(3, 1, 9)
        self.D = Square(30, 6, 7, 13)

    def tearDown(self):
        """tear down test objects"""
        del self.A
        del self.B
        del self.C
        del self.D

    def test_area(self):
        """checks the output of area( with various inputs)"""
        self.assertEqual(self.B.area(), 4)
        self.assertEqual(self.C.area(), 9)
        self.assertEqual(self.D.area(), 900)
    
    def test_display(self):
        """checks that the visual of the rectangle matches its measurements"""
        
        captured_output = StringIO()
        sys.stdout = captured_output
        self.B.display()
        sys.stdout = sys.__stdout__
        expected = "\n ##\n ##\n" 
        self.assertEqual(expected, captured_output.getvalue())

        r1 = Square(5, 2, 2)
        captured_output = StringIO()
        sys.stdout = captured_output
        r1.display()
        sys.stdout = sys.__stdout__  
        expected = "\n\n  #####\n  #####\n  #####\n  #####\n  #####\n"
        self.assertEqual(captured_output.getvalue(), expected)

    @patch('builtins.print')
    def test_square_str_method(self, mock_output):
        """checks that the output of `str()` matches the requirements"""
        A_str = f"[Square] ({self.A.id}) {self.A.x}/{self.A.y} - {self.A.width}"
        output_of_str = str(self.A)
        print(self.A)
        self.assertEqual(output_of_str, A_str)
        mock_output.assert_called_once_with(self.A)

        C_str = f"[Square] ({self.C.id}) {self.C.x}/{self.C.y} - {self.C.width}"
        output_of_str = str(self.C)
        print(self.C)
        self.assertEqual(output_of_str, C_str)
        self.assertEqual(output_of_str, C_str)
        mock_output.assert_called_with(self.C)

    def test_square_update_args(self):
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
        self.assertEqual(self.C.x, 8)

        self.D.update(21, 6, 4, 2)
        self.assertEqual(self.D.id, 21)
        self.assertEqual(self.D.x, 4)
        self.assertEqual(self.D.y, 2)
