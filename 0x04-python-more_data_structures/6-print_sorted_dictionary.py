#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for keys, element in sorted(a_dictionary.items()):
        print("{}: {}".format(keys, element))
