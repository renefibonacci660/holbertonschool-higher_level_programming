#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    total = 0
    divisor = 0
    for index in my_list:
        total = total + (index[0] * index[-1])

        divisor = divisor + index[1]
    return (total/divisor)
