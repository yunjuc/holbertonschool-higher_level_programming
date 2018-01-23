#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Create a Rectangle class based on Base'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Square instantiation'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''define rectangle __str__ output'''
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
               self.y, self.width)

    @property
    def size(self):
        '''size getter'''
        return self.width

    @size.setter
    def size(self, value):
        '''size setter'''
        self.width = value

    def update(self, *args, **kwargs):
        '''update square attributes'''
        if args is not None and len(args) != 0:
            for i, v in enumerate(args):
                if i == 0:
                    self.id = v
                if i == 1:
                    self.size = v
                if i == 2:
                    self.x = v
                if i == 3:
                    self.y = v
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        '''dict representation of square'''
        attr = ['id', 'size', 'x', 'y']
        s_dict = {}
        for k in attr:
            s_dict[k] = getattr(self, k)
        return s_dict
