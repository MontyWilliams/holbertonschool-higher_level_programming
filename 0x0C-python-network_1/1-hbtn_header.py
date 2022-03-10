#!/usr/bin/python3
"""sends a request to the URL and displays the value of variable
"""

if __name__ == "__main__":
    import urllib.request
    from sys import argv

    url = argv[1]
    with urllib.request.urlopen(url) as response:
        html = response.info()
    x = html.get("X-Request-Id")
    print(x)
