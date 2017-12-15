#!/usr/bin/python3
def multiply_by_2(my_dict):
    new_dict = my_dict.copy()
    for i in new_dict:
        new_dict[i] = new_dict[i] * 2
    return new_dict
