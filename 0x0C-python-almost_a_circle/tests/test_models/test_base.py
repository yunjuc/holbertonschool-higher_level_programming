#!/usr/bin/python3
'''test_base unittest module'''
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    '''Unittest for Base model'''

    def test_id_no_value(self):
        '''check id increent when no value is assigned'''
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_with_value(self):
        '''check id increment when assigned'''
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_to_json_string(self):
        '''check dict to json string'''
        obj_dict = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_dict = Base.to_json_string(obj_dict)
        self.assertEqual(json.dumps(obj_dict), json_dict)
        self.assertEqual(type(json_dict), str)
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_save_to_file_rect(self):
        '''check save rectangle to json file'''
        r1 = Rectangle(10, 7)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as file:
                j_load = json.load(file)
        self.assertEqual(type(j_load), list)
        for i in j_load:
            self.assertEqual(dict(i), r1.to_dictionary())

    def test_save_to_file_rect_empty(self):
        '''check save rectangle to json file'''
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
                j_load = json.load(file)
        self.assertEqual(j_load, [])

    def test_save_to_file_rect_none(self):
        '''check save rectangle to json file'''
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
                j_load = json.load(file)
        self.assertEqual(j_load, [])

    def test_save_to_file_square(self):
        '''check save square to json file'''
        s1 = Square(10)
        Square.save_to_file([s1])
        with open("Square.json", "r") as file:
                j_load = json.load(file)
        self.assertEqual(type(j_load), list)
        for i in j_load:
            self.assertEqual(dict(i), s1.to_dictionary())

    def test_save_to_file_square_empty(self):
        '''check save square to json file'''
        Square.save_to_file([])
        with open("Square.json", "r") as file:
                j_load = json.load(file)
        self.assertEqual(j_load, [])

    def test_save_to_file_square_none(self):
        '''check save square to json file'''
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
                j_load = json.load(file)
        self.assertEqual(j_load, [])

    def test_from_json_string(self):
        '''check json string return to list'''
        obj_dict = {"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}
        j_string = Base.to_json_string(obj_dict)
        j_load = Base.from_json_string(j_string)
        self.assertEqual(obj_dict, j_load)
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string([]), [])

    def test_create_rectangle(self):
        '''create a rectangle instance'''
        r1 = Rectangle(3, 5, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_create_square(self):
        '''create an instance by id'''
        s1 = Square(4, 3, 8)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)

    def test_load_from_file_rect(self):
        '''check create rectangle from file'''
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        load = Rectangle.load_from_file()
        for i in load:
            self.assertEqual(str(r1), str(i))
            self.assertIsNot(r1, i)

    def test_load_from_file_square(self):
        '''check create square from file'''
        s1 = Square(10, 7, 2)
        Square.save_to_file([s1])
        load = Square.load_from_file()
        for i in load:
            self.assertEqual(str(s1), str(i))
            self.assertIsNot(s1, i)
