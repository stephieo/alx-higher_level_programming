#!/usr/bin/python3
"""contains a function that writes a python object into a json file"""


import json


def save_to_json_file(my_obj, filename):
    """writes object to json file
    Args:
        my_obj (obj): any python object
        filename (file): a json file
    """
    with open(filename, "w") as x:
        json.dump(my_obj, x)
