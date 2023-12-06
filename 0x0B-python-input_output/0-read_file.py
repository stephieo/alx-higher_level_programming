#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """opens a file and reads it
    Args:
        filename (str): name of file
        """
    with open(filename, encoding='utf-8') as f:
        print(f.read())
