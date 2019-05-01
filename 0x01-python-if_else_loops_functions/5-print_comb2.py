#!/usr/bin/python3
for i in range(0, 99):
    if i < 10:
        print("0", end="")
    print("{:d}, ".format(i), end="" if i <= 97 else "{:d}\n".format(99))
