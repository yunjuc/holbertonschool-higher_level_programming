#!/usr/bin/python3
'''test_rectangle unittest module'''
import unittest
import json
import sys
import os
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    '''Unittest for Rectangle model'''

    def test_id_assignment(self):
        '''create a new rectangle'''
        Base._Base__nb_objects = 0
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        r3 = Rectangle(1, 4, 2, 4, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    def test_width_string(self):
        '''check width is string'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle('a', 2)

    def test_width_float(self):
        '''check width is float'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r2 = Rectangle(1.5, 2)

    def test_width_list(self):
        '''check width is list'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r3 = Rectangle([1], 2)

    def test_height_string(self):
        '''check height is string'''
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(1, 'a')

    def test_height_float(self):
        '''check height is float'''
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(1, 1.5) 

    def test_height_list(self):
        '''check height is list'''
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(1, [1])
 
    def test_x_string(self):
        '''check x is string'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(1, 2, 'x', 4)

    def test_x_float(self):
        '''check x is float'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(1, 2, 1.5, 4)
 
    def test_x_list(self):
        '''check x is list'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(1, 2, [4], 4)
 
    def test_y_string(self):
        '''check y is string'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(1, 2, 3, '4')

    def test_y_float(self):
        '''check y is float'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(1, 2, 4, 4.5)
 
    def test_y_list(self):
        '''check y is list'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(1, 2, 3, [4])
 
    def test_width_zero(self):
        '''check width is 0'''
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1 = Rectangle(0, 2)

    def test_width_negative(self):
        '''check width is negative'''
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1 = Rectangle(-1, 2)
 
    def test_height_zero(self):
        '''check height is 0'''
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1 = Rectangle(1, 0)

    def test_height_negative(self):
        '''check height is negative'''
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r2 = Rectangle(1, -2)

    def test_x_value_error(self):
        '''check x is negative'''
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1 = Rectangle(1, 2, -1, 3)

    def test_y_value_error(self):
        '''check y is negative'''
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1 = Rectangle(1, 2, 3, -4)

    def test_missing_arugment(self):
        '''check missing 1 argument'''
        with self.assertRaises(TypeError):
            r1 = Rectangle(2)

    def test_no_arugment(self):
        '''check no argument'''
        with self.assertRaises(TypeError):
            r2 = Rectangle()

    def test_area_result(self):
        '''check area method'''
        self.assertEqual(Rectangle(2, 4).area(), 8)

    def teset_display_width_height(self):
        '''check rectangle display'''
        r = Rectangle(3, 2)
        display = "###\n###\n"
        output = io.StringIO()
        sys.stdout = output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getValue(), display)

    def teset_display_width_height_x(self):
        '''check rectangle display'''
        r = Rectangle(3, 2, 1)
        display = " ###\n ###\n"
        output = io.StringIO()
        sys.stdout = output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getValue(), display)

    def teset_display_width_height_x_y(self):
        '''check rectangle display'''
        r = Rectangle(3, 2, 1, 2)
        display = "\n\n ###\n ###\n"
        output = io.StringIO()
        sys.stdout = output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getValue(), display)

    def test_str(self):
        '''check __str__ output'''
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_arg(self):
        '''check update method with arg'''
        r = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(str(r), "[Rectangle] (10) 10/10 - 10/10")
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")
        r.update(89, 1, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 1/2")
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")
        r.update(90, 6, 7, 8, 9, 10)
        self.assertEqual(str(r), "[Rectangle] (90) 8/9 - 6/7")
        r.update()
        self.assertEqual(str(r), "[Rectangle] (90) 8/9 - 6/7")

    def test_update_kwarg(self):
        '''check update method with kwarg'''
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=1)
        self.assertEqual(str(r), "[Rectangle] (10) 10/10 - 1/10")
        r.update(id=100, height=2, x=4, y=5)
        self.assertEqual(str(r), "[Rectangle] (100) 4/5 - 1/2")
        r.update(area=24)
        self.assertEqual(str(r), "[Rectangle] (100) 4/5 - 1/2")

    def test_dict(self):
        '''check rectangle dict attributes'''
        r1 = Rectangle(10, 2, 1, 9, 1)
        self.assertEqual(r1.to_dictionary(), {'x': 1, 'y': 9, 'id': 1,
                         'height': 2, 'width': 10})
        self.assertEqual(type(r1.to_dictionary()), dict)
