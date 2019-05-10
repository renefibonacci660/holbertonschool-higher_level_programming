#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_set = set()
    if my_list:
        for element in my_list:
            new_set.add(element)
    return sum(new_set)
