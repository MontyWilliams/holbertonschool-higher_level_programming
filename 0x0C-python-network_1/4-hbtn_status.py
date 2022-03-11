#!/usr/bin/python3
""" this script fetches 
"""


from cgitb import text


if __name__ == '__main__':
    from requests import get
    from urllib import request

    request = get("https://intranet.hbtn.io/status")
    text = request.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
