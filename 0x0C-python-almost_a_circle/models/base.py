#!/usr/bin/python3
import json


class Base:
    '''Define Base class'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''instantiation base instatnce'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''convert dict representation to json string'''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''save dict representation to json file'''
        filename = cls.__name__ + '.json'
        ob_list = []
        if list_objs is None:
            pass
        else:
            for i in list_objs:
                ob_list.append(i.to_dictionary())
        with open(filename, 'w') as f:
            return json.dump(ob_list, f)

    @staticmethod
    def from_json_string(json_string):
        '''convert lis tof json string to dictionary'''
        ob_dict = []
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''create an instance from a list of dictionary'''
        temp = cls(1, 1)
        temp.update(**dictionary)
        return temp
#        return cls(temp.id, temp.width, temp.height, temp.x, temp.y)

    @classmethod
    def load_from_file(cls):
        '''create an instance from json file'''
        filename = cls.__name__ + '.json'
        with open(filename) as f:
            ob_dict = json.load(f)
        ob_list = []
        for i in ob_dict:
            ob_list.append(cls.create(**i))
        return ob_list
