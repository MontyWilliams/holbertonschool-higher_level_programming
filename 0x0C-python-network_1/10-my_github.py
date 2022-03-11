#!/usr/bin/python3
"""
script that fetches https://api.github.com/user
"""


if __name__ == "__main__":
    from sys import argv
    from requests.auth import HTTPBasicAuth
    import requests

    token = argv[2]
    user = argv[1]
    url = "https://api.github.com/user"

    r = requests.get(url, auth=HTTPBasicAuth(user, token)).json()
    print(r.get('id'))
