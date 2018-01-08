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

    def test_empty_list(self):
        '''Empty list'''
        result = max_integer([])
        self.assertEqual(result, None)

    def test_negative(self):
        '''Negative value'''
        result = max_integer([-2, -1, -3])
        self.assertEqual(result, -1)

if __name__ == "__main__":
    unittest.main()
