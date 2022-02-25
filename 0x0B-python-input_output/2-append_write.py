#!/usr/bin/python3
""" task 2-append_write.py
"""


def append_write(filename="", text=""):
    """open file and write to it
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
