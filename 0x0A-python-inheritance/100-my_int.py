#!/usr/bin/python3
'''
    MyInt is a rebel. MyInt has == and != operators inverted
'''


class MyInt(int):
    def __eq__(self, val):
        return (self.number != val)

    def __str__(self):
        return (str(self.number))

    def __init__(self, number):
        self.number = number

    def __ne__(self, val):
        return (self.number == val)
