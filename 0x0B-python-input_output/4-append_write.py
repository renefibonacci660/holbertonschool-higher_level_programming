#!/usr/bin/python3
'''
    contains module append_write
'''


def append_write(filename="", text=""):
    '''
        appends string to textfile
    '''
    with open(filename, mode='a', encoding='utf-8') as a_file:
        stringAdd = a_file.write(text)
    return stringAdd
