#!/usr/bin/python3
'''
    contains methon to_json_string
'''
import json


def to_json_string(my_obj):
    '''
        returns the JSON representation of an obj (string)
    '''
    return (json.dumps(my_obj))
