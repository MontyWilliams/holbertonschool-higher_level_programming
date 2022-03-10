#!/usr/bin/python3
"""fetch url status
"""
if __name__ == "__main__":
    from  urllib import request

    with request.urlopen('https://api.github.com/events') as response:
        html = response.read()
    # print("Body response:")
    # print("\t- type: {}".format(type(html)))
    # print("\t- content: {}".format(html))
    # print("\t- utf8 content: {}".format(html.decode('UTF8')))
