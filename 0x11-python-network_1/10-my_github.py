#!/usr/bin/python3
""" script to access github API using basic authentication"""

from sys import argv
import requests

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]

    req = requests.get(" https://api.github.com/user", auth=(user, passwd))

    print(req.json().get("id"))
