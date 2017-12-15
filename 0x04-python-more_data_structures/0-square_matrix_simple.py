#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = list.copy(matrix)
    for row in new:
        for x, y in enumerate(row):
            row[x] = y * y
    return new
