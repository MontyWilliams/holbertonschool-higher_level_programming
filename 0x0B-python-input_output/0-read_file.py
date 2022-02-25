#!/usr/bin/python3
"""task 0-read_file.py
"""


def read_file(filename=""):
    """read a file and print to stdout
    """
    with open(filename) as f:
        print(f.read(), end="")
