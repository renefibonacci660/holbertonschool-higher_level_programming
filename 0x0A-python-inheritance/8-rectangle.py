#!/usr/bin/python3
'''
    implements geometry class
'''


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''
        implements a rectangle (width/height private)
        both validated to be positive ints
    '''
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
