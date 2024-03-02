#!/usr/bin/python3
""" This module fetches a url using urllib"""

from urllib import request
from urllib import parse

if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        body = response.read()

    print("""Body response:
                - type: {}
                - content: {}
                - utf8 content: {}""".
          format(type(body), body, body.decode("UTF-8")))
