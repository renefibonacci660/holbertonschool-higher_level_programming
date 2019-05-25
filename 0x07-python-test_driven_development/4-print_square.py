#!/usr/bin/python3
'''
    contains function print_square
'''


def print_square(size):
    '''
        prints square in dimentions of size
        size: number of row/length
    '''
    value_err = "size must be >= 0"
    type_err = "size must be an integer"
    if isinstance(size, float) and size < 0:
        raise TypeError(type_err)
    if size < 0:
        raise ValueError(value_err)
    if not isinstance(size, int):
        raise TypeError(type_err)
    print((("#" * size + "\n") * size), end="")
