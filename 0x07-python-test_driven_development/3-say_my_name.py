#!/usr/bin/python3
'''Module: 3-say_my_name
'''


def say_my_name(first_name, last_name=""):
    '''say_my_name: print a name

    ** Args **
       @first_name(str): first name
       @last_name(str, optional): last name

    ** Example **
    >>> say_my_name("John", "Smith")
    My name is John Smith
    '''
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
