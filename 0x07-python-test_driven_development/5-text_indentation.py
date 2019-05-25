#!/usr/bin/python3
'''
    Contains function text_indentation
    two newlines added when ? : or . found
'''


def text_indentation(text):
    '''
        adds two newlines when ? : or . found
        text - must be string to add newlines
    '''
    length = len(text)
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    print(i)
    while i < length:
        {
            print()
        if text[i] == '?' or text[i] == ':' or text[i] == '.':
            print("{}\n\n", format(text[i]))
        else
            print("{}", format(text[i]))
            i = i + 1
        }
