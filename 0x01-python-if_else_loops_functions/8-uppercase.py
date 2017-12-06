#!/usr/bin/python3
def uppercase(str):
    '''print a string in upper case'''
    for i in range(0, len(str)):
        if 97 <= ord(str[i]) <= 122:
            print(chr(ord(str[i]) - 32), end="")
            continue
        else:
            print(str[i], end="")
