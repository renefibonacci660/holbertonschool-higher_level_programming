#!/usr/bin/python3
'''
    Contains class "Square" imports Rectangle
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
        Inherits from class "Rectangle"
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''
            Class constructor
        '''
        super().__init__(size, size, x, y, id)
        '''
            super class that uses init logic in "Rectangle" class
            width and height assigned to value 'size'
        '''

    @property
    def size(self):
        '''
            "Getter" method that returns private attribute
            (var size)
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''
            "Setter" method that checks/sets value of private attributes
            (int val of width/height in that order)
        '''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''
            Updates key/value arguments in class "Square" by
            assigning each to an attribute
        '''
        if args:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        elif len(args) == 0:
            for index, value in kwargs.items():
                self.__setattr__(index, value)
                # alternative to setattr because it may bypass getter/setter?

    def to_dictionary(self):
        '''
            Public method that returns dictionary representation of "Square"
            {} for dictionary
        '''
        return {'x': self.x, 'y': self.y, 'id': self.id, 'size': self.size}

    def __str__(self):
        '''
            Str method overwrites message initially in "Rectangle"
        '''
        return '[Square] ({}) {}/{} - {}'.format(self.id,
                                                 self.x, self.y, self.width)
