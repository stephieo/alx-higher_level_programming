#!/usr/bin/python3
""""unittest for `Base.py` module"""
import unittest
from models.base import Base

# tests:
# -documentation(module, class, method)
# -check that id is incrementing properly
#    #with input
#    #without input (id=None)


class TestBaseClass(unittest.TestCase):
    """tests the functionality of the 'Base` class"""
    # def test_documentation(self):
    #     """check for module, class and method documentation"""
    #     self.assertGreater(len(print(__import__
    #   ("base").my_function.__doc__)), 1)
    #     self.assertGreater(len(print(__import__("base").
    #    MyClass.my_function.__doc__)), 1)
    #     self.assertGreater(len(print(__import__("base").__doc__)), 1)
    #     self.assertGreater(len(print(__import__("base").MyClass.__doc__)), 1)

    def setUp(self):
        """set up test objects"""
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()

    def tearDown(self):
        """set up test objects"""
        del self.b1
        del self.b2
        del self.b3

    def test_id_empty(self):
        """check id is being created properly"""
        self.assertEqual(self.b1.id, 1)

    def test_id_input(self):
        """check id id created when there is  an  input"""
        self.assertEqual(self.b2.id, 2)

    def test_id_neg_input(self):
        self.assertEqual(self.b3.id, 3)
    
