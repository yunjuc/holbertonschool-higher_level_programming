#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    '''Create a Rectangle class based on Base'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Rectangle instantiation'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''width getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''width setter'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
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
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        '''x getter'''
        return self.__x

    @x.setter
    def x(self, value):
        '''x setter'''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        '''y getter'''
        return self.__y

    @y.setter
    def y(self, value):
        '''y setter'''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        '''Calculate rectangle area'''
        return self.width * self.height

    def display(self):
        '''print rectange with character #'''
        for down in range(self.y):
            print()
        for row in range(self.height):
            for right in range(self.x):
                print(" ", end="")
            for col in range(self.width):
                print('#', end="")
            print()

    def __str__(self):
        '''define rectangle __str__ output'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
               self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        '''update rectangle attributes'''
        if args is not None and len(args) != 0:
            for i, v in enumerate(args):
                if i == 0:
                    self.id = v
                if i == 1:
                    self.width = v
                if i == 2:
                    self.height = v
                if i == 3:
                    self.x = v
                if i == 4:
                    self.y = v
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        '''dict representation of rectangle'''
        attr = ['id', 'width', 'height', 'x', 'y']
        rect_dict = {}
        for k in attr:
            rect_dict[k] = getattr(self, k)
        return rect_dict
