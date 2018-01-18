#!/usr/bin/python3


class Student:
    '''A Student class'''

    def __init__(self, first_name, last_name, age):
        '''instantiation new student'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        '''retrieve __dict__ based on attributes'''
        s_dict = {}
        if attr is None:
            s_dict = self.__dict__
        else:
            for key in attr:
                if key in self.__dict__:
                    s_dict[key] = self.__dict__[key]
        return s_dict

    def reload_from_json(self, json):
        '''replace attributes of student instance from JSON file'''
        for key in json:
            self.__dict__[key] = json[key]
