#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle class from BaseGeometry'''

    def __init__(self, width, height):
        '''Rectangle instantiation'''
        self.__widht = width
        self.__height = height
        Rectangle.integer_validator(self, "width", width)
        Rectangle.integer_validator(self, "height", height)
