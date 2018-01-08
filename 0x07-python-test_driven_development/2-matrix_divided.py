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
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix or type(matrix) is not list or type(matrix[0]) is not list\
       or type(matrix[1]) is not list:
        raise TypeError(msg)
    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    for row in matrix:
        new.append(list(map(lambda x: round(x/div, 2), row)))
    return new
