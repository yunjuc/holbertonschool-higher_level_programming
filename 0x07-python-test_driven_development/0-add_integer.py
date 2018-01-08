#!/usr/bin/python3
'''Module: 0-add_integer
'''


def add_integer(a, b):
    '''add_integer: add two integers and return the result

    ** Args **
       @a(int or float): first number
       @b(int or float): second number

    ** Return **
       a + b

    ** Example **
    >>> add_integer(1, 2)
    3
    '''
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
