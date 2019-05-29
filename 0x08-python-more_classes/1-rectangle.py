#!/usr/bin/python3
'''
    contains class Retangle
'''


class Rectangle:
    '''
    Rectangle contains getters and setters
    with initialized variables for width/height
    '''
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def height(self):
        '''
        Returning private variable
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
            Checking for TypeError & ValueError
            then sets up private variable (height)
        '''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        '''
            Returning private variable
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
            Checking for TypeError & ValueError
            then sets up private variable (width)
        '''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value
