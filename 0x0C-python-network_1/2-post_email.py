#!/usr/bin/python3
"""sends POST request to URL with email as parameter
"""


from base64 import decode


if __name__ == "__main__":
    import urllib.request
    from urllib.parse import urlencode
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    Npayload = urlencode(payload).encode('utf-8')
    with urllib.request.urlopen(url, Npayload) as response:
        print(response.read().decode('utf-8'))
