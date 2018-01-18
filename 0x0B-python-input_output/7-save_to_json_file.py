#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    '''convert object to JSON string and save in a file'''
    with open(filename, mode="w") as f:
        return json.dump(my_obj, f)
