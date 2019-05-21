#!/usr/bin/python3
class Square():
    """ A square class """
    def __init__(self, size=0, position=(0, 0)):
        """ Initializing class """
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """ property position """
        return self.__position

    @position.setter
    def position(self, value):
        """property setter position"""
        if not isinstance(value, tuple) and len(value) == 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__position = value

    @property
    def size(self):
        """ defining property size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Defining property setter """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Initializing area calc """
        return self.__size * self.__size

    def my_print(self):
        """ Initializing printing square """
        if self.__size <= 0:
            print()

        else:
            print(((((" " * self.__position[0]) +
                    ("#" * self.__size) + '\n')) * self.__size), end="")
