#!/usr/bin/python3
""" My list class """


class MyList(list):
    """init the class """
    def __init__(self):
        """ init method """
        super().__init__()

    def print_sorted(self):
        """ print list in ascending order"""
        print(sorted(self))
