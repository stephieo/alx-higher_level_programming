#!/usr/bin/python3
"""contains a function that writes a string to a file"""


def write_file(filename="", text=""):
    """writes to a file and returns number of characters written"""
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
