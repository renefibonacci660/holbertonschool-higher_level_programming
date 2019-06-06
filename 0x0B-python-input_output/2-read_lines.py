#!/usr/bin/python3
'''
    contains methond read_lines
'''


def read_lines(filename="", nb_lines=0):
    '''
        reads lines and writes to stdout if nb_lines is
        greater or equal to the total number of lines of the file
    '''
    with open(filename, mode='r', encoding='utf-8') as a_file:
        if nb_lines <= 0:
            print(a_file.read(), end="")
            return
        for line in a_file:
            print(line, end="")
            nb_lines -= 1
            if nb_lines <= 0:
                break
