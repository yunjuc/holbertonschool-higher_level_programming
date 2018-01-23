#!/usr/bin/python3
import unittest
import json
import sys
import os
from models.square import Square
from models.base import Base
from models. rectangle import Rectangle


class TestSquare(unittest.TestCase):
    '''Unittest for Square model'''

    def test_new_square(self):
        '''create square with different arguments'''
        s1 = Square(5)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3, 3)
        self.assertEqual(s1.area(), 25)
        self.assertEqual(s2.area(), 4)
        self.assertEqual(s3.area(), 9)
        self.assertEqual(str(s3), "[Square] (3) 1/3 - 3")
        with self.assertRaises(TypeError):
            s = Square()

#    def test_display(self):
#        '''check square display'''

    def test_size_int(self):
        '''check size type'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1 = Square('a')
            s2 = Square([3])
            s3 = Square(1.5)

    def test_x_int(self):
        '''check x type'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1 = Square(3, '4')
            s2 = Square(3, [3])
            s3 = Square(3, 1.5)

    def test_y_int(self):
        '''check y type'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1 = Square(3, 2, '4')
            s2 = Square(3, 1, [3])
            s3 = Square(3, 3, 1.5)

    def test_size_value(self):
        '''check size value'''
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1 = Square(0)
            s2 = Square(-3)

    def test_x_value(self):
        '''check x value'''
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s1 = Square(3, -3)

    def test_y_value(self):
        '''check y value'''
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s1 = Square(3, 4, -3)

    def test_update_arg(self):
        '''check update method with arg'''
        s = Square(10, 10, 10, 10)
        self.assertEqual(str(s), "[Square] (10) 10/10 - 10")
        s.update(89)
        self.assertEqual(str(s), "[Square] (89) 10/10 - 10")
        s.update(89, 1)
        self.assertEqual(str(s), "[Square] (89) 10/10 - 1")
        s.update(89, 1, 2, 3)
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")
        s.update(90, 6, 7, 8)
        self.assertEqual(str(s), "[Square] (90) 7/8 - 6")
        s.update()
        self.assertEqual(str(s), "[Square] (90) 7/8 - 6")

    def test_update_kwarg(self):
        '''check update method with kwarg'''
        s = Square(10, 10, 10, 10)
        s.update(size=1)
        self.assertEqual(str(s), "[Square] (10) 10/10 - 1")
        s.update(id=100, size=2, x=4, y=5)
        self.assertEqual(str(s), "[Square] (100) 4/5 - 2")
        s.update(area=24)
        self.assertEqual(str(s), "[Square] (100) 4/5 - 2")

    def test_dict(self):
        '''check square dict attributes'''
        s1 = Square(10, 2, 1, 1)
        self.assertEqual(s1.to_dictionary(), {'id': 1, 'x': 2, 'size': 10,
                         'y': 1})
        self.assertEqual(type(s1.to_dictionary()), dict)
