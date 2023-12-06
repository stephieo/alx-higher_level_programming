#!/usr/bin/python3
"""contains a function that appends to a file"""


def append_write(filename="", text=""):
    with open(filename, a, encdoding='utf-8') as file:
        return file.append(text)
