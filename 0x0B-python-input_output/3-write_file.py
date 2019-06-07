#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, mode='w', encoding='utf-8') as a_file:
        charCnt = a_file.write(text)
    return charCnt
