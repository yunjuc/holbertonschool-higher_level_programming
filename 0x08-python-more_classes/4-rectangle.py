#!/usr/bin/python3


class Rectangle:
    '''Define a class Rectangle'''

    def __init__(self, width=0, height=0):
        '''Create new Rectangle object'''
        self.width = width
        self.height = height

    def __str__(self):
        '''Define rectangle string'''
        string = ""
        for i in range(self.__height):
            for j in range(self.__width):
                string += '#'
            if i < self.__height - 1:
                string += '\n'
        return string

    def __repr__(self):
        '''Define rectangle representation'''
        return "Rectangle(" + str(self.__width) + ", " + \
               str(self.__height) + ")"

    @property
    def width(self):
        '''width getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''width setter'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''height getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height setter'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Calculate rectangle area'''
        return self.__width * self.__height

    def perimeter(self):
        '''Calculate rectangel perimeter'''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height)*2
