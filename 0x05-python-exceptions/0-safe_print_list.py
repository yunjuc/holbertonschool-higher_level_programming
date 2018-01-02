#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0
    try:
        for i in my_list:
            if num < x:
                print('{}'.format(i), end="")
                num += 1
        print()
    except IndexError:
        print('Error: index out of range')
    return num
