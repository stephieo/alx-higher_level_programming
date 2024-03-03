#!/usr/bin/python3
""" script to send a POST request to a URL with a parameter"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        letter = ""
    else:
        letter = argv[1]

        r = requests.post("http://0.0.0.0:5000/search_user",
                          data={"q": letter})
        # capture the json response as a dict

        r_json = r.json()
        if r_json == {}:
            print("No result")
        elif not isinstance(r_json, dict):
            print("Not a valid JSON")
        else:
            print(f"[{r.headers.get('id')}] {r}")
