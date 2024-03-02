#!/usr/bin/python3
""" This module fetches a url using urllib"""

from urllib import request
from urllib import parse

if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        body = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode("UTF-8")))
