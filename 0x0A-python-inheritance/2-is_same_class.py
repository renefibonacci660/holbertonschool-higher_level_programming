#!/usr/bin/python3
def is_same_class(obj, a_class):
    '''
        if object is exactly an instance of the specified class
        Returns True else False
    '''
    if type(obj) is a_class:
        return(True)
    return(False)
