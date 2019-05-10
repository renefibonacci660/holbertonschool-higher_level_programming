#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for key, element in a_dictionary.items():
        new_dict.update({key: (element * 2)})
    return new_dict
