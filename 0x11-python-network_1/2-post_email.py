#!/usr/bin/python3
""" This module sends a POST request to a given
    URL and displays the value of a variable in the header
    """
from sys import argv
from urllib import request, parse

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    params = {"email": email}
    querystring = parse.urlencode(params)
    querystring = querystring.encode('ascii')
    req = request.Request(url, data=querystring)


    with request.urlopen(req) as response:
        body = response.read()
        print(f"Your email is: {body.decode('UTF-8')}")




