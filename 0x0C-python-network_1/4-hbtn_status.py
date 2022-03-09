#!/usr/bin/python3
""" this script fetches 
"""


if __name__ == '__main__':
    import requests

    a = 'https://intranet.hbtn.io/status'
    html = requests.get(a)
    print("Body response:")
    print("\t- type: {}".format(type(html.text)))
    print("\t- content: {}".format(html.text))
