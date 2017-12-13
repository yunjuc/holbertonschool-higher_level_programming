#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return NONE
    elif idx > len(my_list):
        return NONE
    else:
        new_list = list.copy(my_list)
        new_list[idx] = element
        return new_list
