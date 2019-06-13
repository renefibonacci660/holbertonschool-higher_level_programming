#!/usr/bin/python3
import unittest
from models.base import Base
fron module.rectangle import Rectangle
import json

'''
    Test cases for the square module
'''


class Test_Square(unittest.TestCase):
    '''
        Testing Square module
    '''
    def test_id_none(self):
        '''
            Sending no id
        '''
        b = Base()
        self.assertEqual(1, b.id)
