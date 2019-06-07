#!/usr/bin/python
'''
    contains methon to_json_string
'''
import json


def to_json_string(my_obj):
    '''
        returns the JSON representation of an object (string)
    '''
    return (json.dumps(my_obj))
