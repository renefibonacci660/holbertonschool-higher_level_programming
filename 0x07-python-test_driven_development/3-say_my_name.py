#!/usr/bin/python3
'''
    contains function say_my_name (prints first last name)
'''


def say_my_name(first_name, last_name=""):
    '''
        Prints "My name is (first last)"
        first_name type string
        last_name type string
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
