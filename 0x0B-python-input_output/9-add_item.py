#!/usr/bin/python3
'''a module to save arguments as list and save it in a JSON file"'''
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    with open(filename, 'r+') as my_list:
        my_list = load_from_json_file(filename)
except:
    my_list = []

i = 1
while i < len(argv):
    my_list.append(argv[i])
    i += 1
save_to_json_file(my_list, filename)
