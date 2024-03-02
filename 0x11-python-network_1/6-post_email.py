#!/usr/bin/python3
""" This module sends a POST request to a given
    URL and displays the body/text of the response
    """
from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    r = requests.post(url, data={"email": email})

    print(r.text)
