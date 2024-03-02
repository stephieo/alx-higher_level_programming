#!/usr/bin/python3
""" This module sends a request to a given
    URL and displays the value of a variable in the header
    """
from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)

    print(r.headers.get('X-Request-Id'))
