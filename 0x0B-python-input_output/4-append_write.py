#!/usr/bin/python3


def append_write(filename="", text=""):
    '''append a string to the end of file(utf8)'''
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
