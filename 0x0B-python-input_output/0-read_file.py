#!/usr/bin/python3
'''
    read_file method
'''


def read_file(filename=""):
    '''
        reads file and prints to stdout
    '''

    with open(filename, mode='r', encoding='utf-8') as a_file:
        print(a_file.read(), end="")
