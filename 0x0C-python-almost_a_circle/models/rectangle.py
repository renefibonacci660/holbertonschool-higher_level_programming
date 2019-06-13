#!/usr/bin/python3
from models.base import Base

'''
    class 'Rectangle that inherits from Base
'''


class Rectangle(Base):
    '''
        Contains private instance attributes each with own
        public getter and setter
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
            Class constructor
        '''

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''
            "Getter" method that returns private attribute
            (var of width)
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
            "Setter" method that check/sets private attribute
            (var of width)
        '''
        if not type(value) == int:
            raise TypeError('width must be an integer')
        if not value > 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        '''
            "Getter" method that returns private attribute
            (var of height)
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
            "Setter" method that checks/sets private attribute
            (var of height)
        '''
        if not type(value) == int:
            raise TypeError('height must be an integer')
        if not value > 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        '''
            "Getter" method that returns private attribute
            (var value of x)
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
            "Setter" method that checks/sets private attribute
            (var value of x)
        '''
        if not type(value) == int:
            raise TypeError('x must be an integer')
        if not value >= 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        '''
            "Getter" method that returns private attribute
            (var value of y)
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
            "Setter" method that checks/sets private attribute
            (var value of y)
        '''
        if not type(value) == int:
            raise TypeError('y must be an integer')
        if not value >= 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        '''
            Public method that returns the area of the "Rectangle" instance
        '''
        return (self.__height * self.__width)

    def display(self):
        '''
            Public method that prints to stdout "Rectangle" instance
            with char "#"
        '''
        print("\n" * self.y, end="")
        rectangle = ""
        for i in range(self.height):
            rectangle += (" " * self.x) + ("#" * self.width) + "\n"
        print(rectangle, end="")

    def update(self, *args, **kwargs):
        '''
            Updates key/value arguments in class "Rectangle" by
            assigning each to an attribute
        '''
        if args:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        elif len(args) == 0:
            for index, value in kwargs.items():
                self.__setattr__(index, value)
                # alternative to setattr because it may bypass getter/setter?
            return

    def to_dictionary(self):
        '''
            Public method that returns dictionary representation of "Rectangle"
            {} for dictionary
        '''
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}

    def __str__(self):
        '''
            Method that overrides class "Rectangle" and returns
            method str message instead
        '''
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y,
                        self.width, self.height))
