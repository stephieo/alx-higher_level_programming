#!/usr/bin/python3
"""contains a function that creates an object from a json file"""


import json


def load_from_json_file(filename):
    """loads object from json file"""
    with open(filename, 'r') as x:
