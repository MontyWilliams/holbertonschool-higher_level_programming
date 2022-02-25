#!/usr/bin/python3
""" task 5 Save Object to a file
"""


import json


def save_to_json_file(my_obj, filename):
    """open the file
    """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
