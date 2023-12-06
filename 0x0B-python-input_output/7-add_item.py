#!/usr/bin/python3
"""populates a list and sves to json file"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

allargs = []

for item in sys.arg:
    allargs.append(item)

save_to_json_file(allargs, "add_item.json")
