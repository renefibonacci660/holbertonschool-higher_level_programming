#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    quotient_list = []
    for index in range(list_length):
        try:
            quotient_list.append(my_list_1[index] / my_list_2[index])
        except(TypeError, ZeroDivisionError, IndexError) as error:
            if (isinstance(error, ZeroDivisionError)):
                print("division by 0")
            elif (isinstance(error, IndexError)):
                print("out of range")
            elif (isinstance(error, TypeError)):
                print("wrong type")
                quotient_list.append(0)
        finally:
            pass
    return quotient_list
