#!/usr/bin/python3
for i in range(0, 10):
    for ii in range(0, 10):
        if (i < ii):
            print("{}{}".format(i, ii), end="")
            if (i <= 7):
                print(", ", end="")
print("\n", end="")
