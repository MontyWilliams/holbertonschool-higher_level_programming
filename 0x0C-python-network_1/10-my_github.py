#!/usr/bin/python3
"""
script that fetches https://api.github.com/user
"""


if __name__ == "__main__":
    import requests
    import sys
    from requests.auth import HTTPBasicAuth

    token = sys.argv[2]
    user = sys.argv[1]
    url = "https://api.github.com/user"

    r = requests.get(url, auth=HTTPBasicAuth(user, token)).json()
    print(r.get('id'))
