#!/usr/bin/python3
"""contains a function that appends to a file"""


def append_write(filename="", text=""):
    """appends to a file
    Args:
        filename (str): name of file to write to
        text (str): text to append
    """
    with open(filename, "a", encdoding='utf-8') as f:
        return f.append(text)
