#!/usr/bin/python3
""" Inherits from the base class
"""
from models.base import Base


class Rectangle(Base):
    """Create rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter
        """
        return self.__width

    @width.setter
    def width(self, width):
        """width setter
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """height getter
        """
        return self.__width

    @height.setter
    def height(self, height):
        """width setter
        """
        if type(height) != int:
            raise TypeError("width must be an integer")
        if height <= 0:
            raise ValueError("width must be > 0")
        self.__height = height

    @property
    def x(self):
        """x getter
        """
        return self.__x

    @x.setter
    def x(self, x):
        """x setter
        """
        if type(x) != int:
            raise TypeError("x must be integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter
        """
        return self.__y

    @y.setter
    def y(self, y):
        """y setter
        """
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ area method
        """
        return self.__width * self.__height

    def display(self):
        """print the square to standard out with #'s
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x, end='')
            print('#' * self.__width)

    def __str__(self):
        """return string rep of a rectangle
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
        self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """Assigns 'args' to each attribute. In order if no args then uses kwargs
        """
        count = 0
        attrs = ['id', 'width', 'height', 'x', 'y']
        if args:
            for arg in args:
                setattr(self, attrs[count], arg)
                count += 1
            for key, value in kwargs.items():
                setattr(self, key, value)
