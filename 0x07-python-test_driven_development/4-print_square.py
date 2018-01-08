#!/usr/bin/python3
'''Module: 4-print_square
'''


def print_square(size):
    '''print_square: print a square

    ** Args **
       @size(int): length of square

    ** Example **
    >>> print_square(3)
    ###
    ###
    ###
    '''
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        for col in range(size):
            print("#", end="")
        print()
