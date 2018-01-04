#!/usr/bin/python3


class Square:
    ''' Create a class Square.'''

    def __init__(self, size=0):
        '''Initialize Square class.

        Args:
        @size: Size of the square
        '''
        self.__size = size

    @property
    def size(self):
        '''Set size as property

        Returns:
        Value of size.
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''Setter of size

        Args:
        @value: value of size
        '''
        if not isinstance(value, int):
            print("size must be an integer", end="")
            raise TypeError
        elif value < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = value

    def area(self):
        '''Caculate the area of a squre.

        Returns:
        Power of square size.
        '''
        return self.__size ** 2
