#!/usr/bin/python3
'''
    Contains one function matrix_divided
'''


def matrix_divided(matrix, div):
    '''
    Divides matrix by given divisor
    matrix: of type list
    div: divisor
    '''

    try:
        length = len(matrix[0])
    except:
        pass

    new_matrix = []
    type_err = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        new_row = []
        if not isinstance(row, list):
            raise TypeError(type_err)
        if length != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for l in row:
            if not isinstance(l, (int, float)):
                raise TypeError(type_err)
            value = round(l / div, 2)
            new_row.append(value)
        new_matrix.append(new_row)
    return new_matrix
