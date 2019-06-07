#!/usr/bin/python3
import sys
save_to_json = __import__("7-save_to_json_file").save_to_json_file
load_from_json = __import__("8-load_from_json_file").load_from_json_file


def add_item(args="", filename=""):
    '''
        contains cript that adds all arguments to a Python list
        and then save them to a file
    '''
    try:
        allArgs = load_from_json(filename)
    except:
        allArgs = []

    for index in args:
        allArgs.append(item)
    save_to_json(allArgs, filename)


if __name__ == "__main__":
    args = sys.argv[1:]
    filename = "add_item.json"
    add_item(args, filename)
# called recursively the method (another use)
