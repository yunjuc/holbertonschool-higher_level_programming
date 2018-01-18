#!/usr/bin/python3


class Student:
    '''A Student class'''

    def __init__(self, first_name, last_name, age):
        '''instantiation new student'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''retrieve __dict__ of student instance'''
        return self.__dict__
