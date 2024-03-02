#!/usr/bin/python3
""" This module fetches a url using the requests package """
import requests

if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")

    print("Body response:")
    print(f"\t- type: {type(r.text)}")
    print(f"\t- content: {r.text}")
