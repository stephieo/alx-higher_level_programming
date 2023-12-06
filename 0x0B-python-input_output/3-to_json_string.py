#!/usr/bin/python3
""" contains a function that gets the JSON representation of an object"""


import json


def to_json_string(my_obj):
    """converts python object to json string"""
    return json.dumps(my_obj)
