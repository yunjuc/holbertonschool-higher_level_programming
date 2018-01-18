#!/usr/bin/python3


def number_of_lines(filename=""):
    '''read a file(UTF8) and return number of lines'''
    count = 0
    with open(filename, encoding="utf-8") as f:
        for line in f:
            count += 1
    return count
