#!/usr/bin/python3


def write_file(filename="", text=""):
    '''write a string to a file(utf8)'''
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
