#!/usr/bin/python3
'''Module: 2-matrix_divided
'''


def matrix_divided(matrix, div):
    '''matrix_divided: divide all elements of a given matrix

    ** Args **
       @matrix(list):a list of matrix, must be int or float
       @div(int or float): divider

    ** Return **
       A new divided list of matrix
    '''
    new = []
    type_err = "matrix must be a matrix (list of lists) of integers/floats"
    len_err = "Each row of the matrix must have the same size"
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(type_err)
    for ele in matrix:
        if type(ele) is not list:
            raise TypeError(type_err)
        for n in ele:
            if type(n) is not int and type(n) is not float:
                raise TypeError(type_err)
        l = len(matrix[0])
        if len(ele) != l:
            raise TypeError(len_err)
    if div is 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    for row in matrix:
        new.append(list(map(lambda x: round(x/div, 2), row)))
    return new
