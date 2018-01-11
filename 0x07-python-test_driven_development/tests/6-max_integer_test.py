#!/usr/bin/python3
'''Unittest for max_integer([..])'''
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''Test max_integer() function'''

    def test_normal(self):
        '''Test a normal list'''
        result = max_integer([1, 3, 3, 2])
        self.assertEqual(result, 3)

    def max_first(self):
        '''Test a normal list'''
        result = max_integer([8, 3, 3, 2])
        self.assertEqual(result, 8)

    def max_end(self):
        '''Test a normal list'''
        result = max_integer([1, 3, 3, 10])
        self.assertEqual(result, 10)

    def one_element(self):
        '''Test a normal list'''
        result = max_integer([5])
        self.assertEqual(result, 5)

    def test_empty_list(self):
        '''Empty list'''
        result = max_integer([])
        self.assertEqual(result, None)

    def test_negative(self):
        '''Negative value'''
        result = max_integer([-2, -1, -3])
        self.assertEqual(result, -1)

    def test_str(self):
        '''Test if list has a string'''
        with self.assertRaises(TypeError):
            max_integer([1, 'hello', 2, 3])

    def test_float(self):
        '''Test if list has float'''
        with self.assertRaises(TypeError):
           max_integer([1, 2, -3, 5.5])


if __name__ == "__main__":
    unittest.main()
