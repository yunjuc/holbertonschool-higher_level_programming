#!/usr/bin/python3
def uppercase(str):
    '''print a string in upper case'''
    for i in range(0, len(str)):
        char = str[i]
        if 97 <= ord(str[i]) <= 122:
            char = chr(ord(str[i]) - 32)
        print("{}".format(char), end="")
    print()
