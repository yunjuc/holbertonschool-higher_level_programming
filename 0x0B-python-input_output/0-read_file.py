#!/usr/bin/python3


def read_file(filename=""):
    '''read a file(UTF8) and print in stdout'''
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
