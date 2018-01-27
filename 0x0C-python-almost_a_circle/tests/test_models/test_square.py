#!/usr/bin/python3
'''test_square unittest module'''
import unittest
from models.square import Square
from models.base import Base
from models. rectangle import Rectangle


class TestSquare(unittest.TestCase):
    '''Unittest for Square model'''

    def test_new_square(self):
        '''check square id'''
        Base._Base__nb_objects = 0
        s1 = Square(5)
        s2 = Square(2, 2)
        s3 = Square(2, 3, 4)
        s4 = Square(3, 1, 3, 22)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s3.y, 4)
        self.assertEqual(s4.id, 22)

    def test_square_area(self):
        '''check area'''
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

    def test_square_str(self):
        '''check square __str__'''
        s3 = Square(3, 1, 3, 3)
        self.assertEqual(str(s3), "[Square] (3) 1/3 - 3")

    def test_no_argument(self):
        '''new instance without arugment'''
        with self.assertRaises(TypeError):
            s = Square()

    def test_size_string(self):
        '''check size is string'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1 = Square('a')

    def test_size_float(self):
        '''check size is float'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s2 = Square(1.5)

    def test_size_list(self):
        '''check size is list'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s3 = Square([1])

    def test_size_zero(self):
        '''check size is 0'''
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1 = Square(0)

    def test_size_negative(self):
        '''check size is negative'''
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s2 = Square(-3)

    def test_x_type(self):
        '''check x is string'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1 = Square(3, 'a')

    def test_x_value(self):
        '''check x value'''
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s1 = Square(3, -3)

    def test_y_type(self):
        '''check y is string'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1 = Square(3, 2, '4') 

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
