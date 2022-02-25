#!/usr/bin/python3
""" ctrate class obj
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square
    """
    def __init__(self, size):
        """ init square as rectangle subclass
        """
        self.integer_validator("size", size)
        self.__size = size
        self.__width = size
        self.__height = size

    def area(self):
        """method returns the area
        """
        return self.__size * self.__size

    def __str__(self):
  
        """method provides string width and height
        """

        return "[Square] {:d}/{:d}".format(self.__width, self.__height)
