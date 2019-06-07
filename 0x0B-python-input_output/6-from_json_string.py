#!/usr/bin/python3
'''
    contains method from_json_string
'''
import json


def from_json_string(my_str):
    '''
        function returns an object
        (Python data structure) represented by a JSON str
    '''
    return json.loads(my_str)
