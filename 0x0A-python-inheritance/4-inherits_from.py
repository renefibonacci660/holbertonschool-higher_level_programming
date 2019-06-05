#!/usr/bin/python3
def inherits_from(obj, a_class):
    '''
        checks if the object is an instance of,
        or if the object is an instance of a class that inherited from,
        the specified class True or False
    '''
    if issubclass(type(obj), a_class) and not type(obj) is a_class:
        return (True)
    return (False)
