#!/usr/bin/python3
import sys
if __name__ == "__main__":
    list = sys.argv
    argStr = len(list) - 1
    totalNumAdd = 0
    if argStr > 0:
            for i in range(len(list)):
                if i != 0 and list[i]:
                    totalNumAdd = totalNumAdd + int(list[i])
    print(totalNumAdd)
