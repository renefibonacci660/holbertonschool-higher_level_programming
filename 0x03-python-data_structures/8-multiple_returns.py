#!/usr/bin/python3
def multiple_returns(sentence):
    str_length = len(sentence)
    if (str_length == 0):
        return (str_length, None)
    return (str_length, sentence[0])
