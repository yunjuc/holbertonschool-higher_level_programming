#!/usr/bin/python3


class BaseGeometry:
    '''an base Geometry class'''

    def area(self):
        '''raise an exception'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validate name and value'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
