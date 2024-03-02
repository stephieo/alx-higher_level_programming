#!/usr/bin/python3
""" This module sends a request to a given
    URL and displays the value of a variable in the header
    """
from sys import argv
from urllib import request

if __name__ == "__main__":
    url = argv[1]
    with request.urlopen(url) as response:
        body = response.read()
        print(response.getheader(""))

