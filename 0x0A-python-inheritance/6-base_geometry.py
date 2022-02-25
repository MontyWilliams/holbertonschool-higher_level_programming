#!/usr/bin/python3
"""add onto base class
"""


class BaseGeometry:
    """dose nothing
    """

    def area(self):
        """this method raises an exception
        """
        raise Exception("area() is not implemented")
