#!/usr/bin/python3
""" This module fetches a url using urllib
    and handles errors"""
from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]

    r = requests.get(url)
    if (r.ok):
        print(r.text)
    else:
        print(f"Error code: {r.status_code}")
