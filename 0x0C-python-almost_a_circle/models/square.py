#!/usr/bin/python3
"""Subclass square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square inherits from rectangle which inherits from Base
    """
    def __init__(self, size, x=0, y=0, id=None):
        """inits from the super class
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for Square size.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for Square size.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
