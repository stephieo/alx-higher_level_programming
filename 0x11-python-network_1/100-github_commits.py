#!/usr/bin/python3
""" script to print the 10 most recent commits using the Github API"""

import requests
from sys import argv

if __name__ == "__main__":
    repo_name = argv[1]
    owner_name = argv[2]

    req = requests.get("https://api.github.com/repos/{}/{}/commits".format(
                       owner_name, repo_name), params={"per_page": 10})

    commit_json = req.json()

    for commit in commit_json:
        sha = commit.get('sha')
        name = commit['commit']['author']['name']
        print(f"{sha}: {name}")
