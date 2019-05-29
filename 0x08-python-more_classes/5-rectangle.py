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

    def area(self):
        '''
            Calculates area of rectangle
        '''
        return self.__width * self.__height

    def perimeter(self):
        '''
            Calculates perimeter of retangle
        '''
        if self.height == 0 or self.width == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        '''
            Returns string of rectangles represented with '#'
        '''
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle
        for height in range(self.__height - 1):
            rectangle += "#" * self.width + "\n"
        rectangle += "#" * self.width
        return rectangle

    def __repr__(self):
        '''
            Returns a str rep of rectangle in order
            to recreate a new instance
        '''
        return "Rectangle(%s, %s)" % (self.__width, self.__height)

    def __del__(self):
        '''
            prints message if instance is deleted
        '''
        print("Bye rectangle...")
