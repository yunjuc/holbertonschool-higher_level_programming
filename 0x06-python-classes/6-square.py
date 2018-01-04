#!/usr/bin/python3


class Square:
    ''' Create a class Square.'''

    def __init__(self, size=0, position=(0, 0)):
        '''Initialize Square class.

        Args:
        @size: Size of the square.
        @poistion: Starting point of the square.
        '''
        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''Set size as property.

        Returns:
        Value of size.
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''Setter of size.

        Args:
        @value: value of size.
        '''
        if not isinstance(value, int):
            print("size must be an integer", end="")
            raise TypeError
        elif value < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = value

    @property
    def position(self):
        '''Set position as property.

        Returns:
        Coordination of position.
        '''
        return self.__position

    @position.setter
    def position(self, value):
        '''Setter of position coordination.

        Args:
        @value: coordination of position.
        '''
        if value[0] < 0 or isinstance(value[0], int) is False or \
           value[1] < 0 or isinstance(value[1], int) is False or \
           len(value) != 2:
            print("position must be a tuple of 2 positive integers", end="")
            raise TypeError
        else:
            self.__position = value

    def area(self):
        '''Caculate the area of a squre.

        Returns:
        Power of square size.
        '''
        return self.__size ** 2

    def my_print(self):
        '''Print a square with character #.'''
        if self.__size == 0:
            print()
        else:
            for y in range(self.__position[1]):
                print()
            for row in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for col in range(self.__size):
                    print("#", end="")
                print()
