#!/usr/bin/python3
import unittest
from models.base import Base
fron module.rectangle import Rectangle
from models.square import Square
import json

'''
    Test cases for the base module
'''


class Test_Base(unittest.TestCase):
    '''
        Testing Base module
    '''
    def test_id_none(self):
        '''
            Sending no id
        '''
        b = Base()
        self.assertEqual(1, b.id)
