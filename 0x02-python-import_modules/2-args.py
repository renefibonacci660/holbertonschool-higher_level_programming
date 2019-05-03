#!/usr/bin/python3
import sys
if __name__ == "__main__":
    list = sys.argv
    argStr = len(list) - 1
    if argStr == 0:
        print("{:d} arguments.".format(argStr))
    elif argStr == 1:
        print("{:d} argument:".format(argStr))
    else:
        print("{:d} arguments:".format(argStr))
    i = 1
    if argStr > 0:
        for i in range(len(list)):
            if i != 0:
                print("{:d}: {}".format(i, list[i]))
