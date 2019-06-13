#!/usr/bin/python3
'''
    This class is the “base” of all other classes in this project
'''

import json


class Base:
    '''
        Purpose is to manage id attribute in all your future classes and
        to avoid duplicating the same code (by extension, same bugs)
        Attributes:
            @id: public instance attribute
            @__nb_objects: private class attribute
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''
            class constructor
        '''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
            Method that writes JSON string rep of list_objs to file
        '''
        file_name = cls.__name__ + ".json"

        fileCopy = []
        if list_objs:
            for instance in list_objs:
                instance = instance.to_dictionary()
                json_dict = json.loads(cls.to_json_string(instance))
                fileCopy.append(json_dict)

        with open(file_name, mode="w", encoding="utf-8") as a_file:
            json.dump(fileCopy, a_file)

    @staticmethod
    def from_json_string(json_string):
        '''
            Static method that returns the list of the JSON str rep json_string
        '''
        if json_string:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        '''
            returns an instance with all attributes already set
        '''
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ is "Rectangle":
            NdicInst = Rectangle(6, 13)
        elif cls.__name__ is "Square":
            NdicInst = Square(7)
        NdicInst.update(**dictionary)
        return (NdicInst)

    @classmethod
    def load_from_file(cls):
        '''
            returns lists of instances
        '''

        file_name = cls.__name__ + ".json"
        instanceList = []
        try:
            with open(file_name, mode="r", encoding="utf-8") as a_file:
                content = cls.from_json_string(a_file.read())
            for i in content:
                instanceList += [cls.create(**i)]
        except:
            return []

        return instanceList
