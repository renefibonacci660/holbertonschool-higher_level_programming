#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for index, i in enumerate(line):
            print("{:d}".format(i), end="")
            if (index < len(line) - 1):
                print("{}".format(" "), end="")
        print()
