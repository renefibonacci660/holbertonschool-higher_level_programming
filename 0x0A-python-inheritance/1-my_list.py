#!/usr/bin/python3
'''
    Inherits attributes from parent class list
'''


class MyList(list):
    '''
        prints the list but in sorted ascending order
    '''
    def print_sorted(self):
        print(sorted(self))
