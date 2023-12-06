#!/usr/bin/python3
""" contains a function that loads a json representation of an object"""


import json


def from_json_string(my_str):
    """converts json string to python object"""
    return json.loads(my_str)
