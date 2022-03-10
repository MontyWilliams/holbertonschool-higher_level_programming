#!/usr/bin/python3
"""sends POST request to URL with email as parameter
"""


if __name__ == "__main__":
    from urllib import request
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    with request.urlopen(url, data=bytes(str(payload), 'utf-8')) as response:
        print(str(response.read(), 'utf-8'))
