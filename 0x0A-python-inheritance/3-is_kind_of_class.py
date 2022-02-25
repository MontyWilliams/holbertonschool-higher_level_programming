#!/usr/bin/python3
"""
python inheritance
"""


def is_kind_of_class(obj, a_class):
    """
    this method checks if an object is an instance of
    or an instance of a class inherited from a_class
    """

    return isinstance(obj, (a_class))
