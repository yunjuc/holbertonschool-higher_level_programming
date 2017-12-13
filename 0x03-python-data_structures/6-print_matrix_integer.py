#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix[0]:
        return print()
    for i in range(len(matrix)):
        j = 0
        for j in range(len(matrix)):
            print("{}".format(matrix[i][j]), end="")
            if j < len(matrix) - 1:
                print(" ", end="")
        print()
