#!/usr/bin/python3
"""populates a list and sves to json file"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    allargs = load_from_json_file("add_item.json")
except Exception:
    allargs = []

allargs.extend(sys.argv[1:])
save_to_json_file(allargs, "add_item.json")
