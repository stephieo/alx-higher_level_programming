#!/usr/bin/python3
"""defines a function that reads a text file to stdout"""


def read_file(filename=""):
    """opens a file and reads it
    Args:
        filename (str): name of file
        """
    with open(filename, encoding='utf-8') as f:
        print(f.read())


read_file("my_file_0.txt")