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

    def integer_validator(self, name, value):
        """check values
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
