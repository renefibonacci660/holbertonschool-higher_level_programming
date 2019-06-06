#!/usr/bin/python3
'''
    importing module for rectangle class
'''
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    '''
        class of square subclass of rectangle
    '''
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2
