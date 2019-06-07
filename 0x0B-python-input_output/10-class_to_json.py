#!/usr/bin/python3
import json


def class_to_json(obj):
    '''
        contains function that returns the dictionary
        description with simple data structure
    '''
    return (getattr(obj, "__dict__"))
