#!/usr/bin/python3
import json


def from_json_string(my_obj):
    '''convert a JSON string to object'''
    return json.loads(my_obj)
