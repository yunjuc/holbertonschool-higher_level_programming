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


class Rectangle(BaseGeometry):
    '''Rectangle class from BaseGeometry'''

    def __init__(self, width, height):
        '''Rectangle instantiation'''
        self.__width = width
        self.__height = height
        Rectangle.integer_validator(self, "width", width)
        Rectangle.integer_validator(self, "height", height)

    def __str__(self):
        '''Rectangle definition'''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        '''define rectangle area'''
        return self.__width * self.__height
