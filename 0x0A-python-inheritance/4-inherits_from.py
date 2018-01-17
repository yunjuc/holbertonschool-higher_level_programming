#!/usr/bin/python3
'''inherits_from module'''


def inherits_from(obj, a_class):
    '''check if an object is sub class of a class'''
    return issubclass(type(obj), a_class) and type(obj) is not a_class
