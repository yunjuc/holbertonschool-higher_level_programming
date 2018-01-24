#!/usr/bin/python3
'''test_base unittest module'''
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    '''Unittest for Base model'''

    def test_id_value(self):
        '''check id increment'''
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_dict_to_json(self):
        '''check dict to json string'''
        obj_dict = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_dict = Base.to_json_string(obj_dict)
        self.assertEqual(json.dumps(obj_dict), json_dict)
        self.assertEqual(type(json_dict), str)
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_string_to_file(self):
        '''check save dict to json file'''
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as file:
                j_load = json.load(file)
        self.assertEqual(type(j_load), list)
        for i in j_load:
            self.assertEqual(dict(i), r1.to_dictionary())

    def test_jstring_to_dict(self):
        '''check json string return to list'''
        obj_dict = {"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}
        j_string = Base.to_json_string(obj_dict)
        j_load = Base.from_json_string(j_string)
        self.assertEqual(obj_dict, j_load)
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string([]), [])

    def test_dict_to_instance(self):
        '''check create instance from dict'''
        r1 = Rectangle(3, 5, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_file_to_instance(self):
        '''check create instance from file'''
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        load = Rectangle.load_from_file()
        for i in load:
            self.assertEqual(str(r1), str(i))
            self.assertIsNot(r1, i)
