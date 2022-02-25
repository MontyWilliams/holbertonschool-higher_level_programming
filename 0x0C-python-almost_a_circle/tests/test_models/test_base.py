#!/usr/bin/python3
from models.base import Base
import unittest
# import pep8
"""unit testing for zhe Base claaaussee
"""

class TestBaseMethods(unittest.TestCase):
    """Testing Base methods class is made and test runs against itslf
    """

    def test_init(self):
        """test the base init method under diff circumstances
        """
        obj1 = Base()
        self.assertEqual(obj1.id, 1)
        obj2 = Base(6300)
        self.assertEqual(obj2.id, 6300)
        obj3 = Base(None)
        self.assertEqual(obj3.id, 2)
        obj4 = Base()
        self.assertEqual(obj4.id, 3)
    

