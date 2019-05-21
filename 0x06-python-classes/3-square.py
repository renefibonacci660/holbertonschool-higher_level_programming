#!/usr/bin/python3
class Square():
    """ A square class """
    def __init__(self, size=0):
        """ Initializing class """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ Initializing area calc """
        return self.__size * self.__size
