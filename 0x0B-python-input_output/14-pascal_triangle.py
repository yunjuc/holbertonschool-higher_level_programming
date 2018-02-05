#!/usr/bin/python3


def pascal_triangle(n):
    '''create lists of integers representing the Pascal’s triangle of n'''
    tri = []
    if n <= 0:
        return tri
    for i in range(0, n):
        row = []
        if i > 0:
            row.append(1)
            j = 1
            while j < i:
                row.append(tri[i-1][j-1]+tri[i-1][j])
                j += 1
        row.append(1)
        tri.append(row)
    return tri
