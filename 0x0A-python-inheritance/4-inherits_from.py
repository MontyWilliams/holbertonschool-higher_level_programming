#!/usr/bin/python3
"""
This module contains the method: inherits_from.
"""


def inherits_from(obj, a_class):
    """
    check if an object, 'obj', is an instance
    of a class that inherited directly or indirectly from
    the specified class.
    """
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
