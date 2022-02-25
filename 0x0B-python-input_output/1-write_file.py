#!/usr/bin/python3
""" task 1-write_file.py
"""


def write_file(filename="", text=""):
    """open file and write to it
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
