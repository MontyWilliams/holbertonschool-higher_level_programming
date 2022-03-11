#!/usr/bin/python3
"""
script that fetches https://api.github.com/user
"""


if __name__ == "__main__":
    from requests import get
    from sys import argv

    requests = get('https://api.github.com/user',
                   auth=(argv[1], argv[2]))
    print(requests.json['id'])

