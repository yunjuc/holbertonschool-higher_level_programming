#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    '''read a file(UTF8) and print number of lines'''
    with open(filename, encoding="utf-8") as f:
        count = 0
        for line in f:
            count += 1
        f.seek(0)
        if nb_lines <= 0 or nb_lines >= count:
            print(f.read(), end="")
        else:
            i = 0
            for line in f:
                if i < nb_lines:
                    print(line, end="")
                i += 1
