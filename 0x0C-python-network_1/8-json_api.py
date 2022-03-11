#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
"""


if __name__ == "__main__":
    from requests import get, post
    from sys import argv

    if len(argv) < 2:
        txt = ""
    else:
        txt = argv[1]
    site = 'http://0.0.0.0:5000/search_user'
    request = post(site, data={'txt': txt})
    try:
        dic = request.json()
        id = dic.get('id')
        name = dic.get('name')
        if len(dic) == 0:
            print("No result")
        else:
            print("[{}] {}".format(id, name))

    except:
        print("Not a valid JSON")
