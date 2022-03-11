#!/usr/bin/python3
""" this script fetches  a response from a url and checks for errors
"""


if __name__ == "__main__":
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError
    from sys import argv

    url = Request(argv[1])
    try:
        with urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as error:
        print("Error code: {}".format(error.code))
