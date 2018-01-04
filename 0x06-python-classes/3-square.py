#!/usr/bin/python3


class Square:
    ''' Create a class Square.'''

    def __init__(self, size=0):
        '''Initialize Square class.

        Args:
            @size: Size of the square
        '''
        if not isinstance(size, int):
            print("size must be an integer", end="")
            raise TypeError
        elif size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = size

    def area(self):
        '''Caculate the area of a squre.

        Returns:
            Power of square size.
        '''
        return self.__size**2
