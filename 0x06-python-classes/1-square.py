#!/usr/bin/python3
"""Defines a Square"""
class Square:
    """class definition of Square"""
    def __init__(self, squaresize=0):
        """initializes instances of Square
        
        Args:
            squaresize(int): length of one side of Square
        """
        self.__size = squaresize
