#!/usr/bin/python3
def uppercase(str):
    for l in str:
        print("{:s}".format(chr(ord(l) - 32)
                          if (ord(l) >= ord("a") and ord(l) <= ord("z")) else l), end="")
    print()
