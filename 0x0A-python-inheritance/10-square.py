#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''define Square class based on Rectangle'''

    def __init__(self, size):
        '''Square instantiation'''
        self.__size = size
        Square.integer_validator(self, "size", size)
        super().__init__(size, size)

    def area(self):
        '''define Square area'''
        return self.__size * self.__size
