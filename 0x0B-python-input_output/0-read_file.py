#!/usr/bin/python3
""" defines a function that reads a text file and prints it to stdout"""


def read_file(filename=""):
    """opens a file and reads it"""
    with open(filename, encoding='utf-8') as f:
        print(f.read())
