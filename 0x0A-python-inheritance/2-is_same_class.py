#!/usr/bin/python3
'''is_same_class module'''


def is_same_class(obj, a_class):
    '''check if an object and a class is the same'''
    if type(obj) is a_class:
        return True
    else:
        return False
