#!/usr/bin/python3
""" This module fetches a url using urllib
    and handles HTTPErrors"""
from sys import argv
from urllib import request
from urllib.error import HTTPError

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            body = response.read()
            print(f"{body.decode('UTF-8')}")
    except HTTPError as error:
        print(f"Error code: {error.status}")
