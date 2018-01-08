#!/usr/bin/python3
'''Module: 5-text_indentation
'''


def text_indentation(text):
    '''text_indentation: print new line after characters ".", ":", and "?"

    ** Args **
       @text(str): source string
    '''
    if type(text) is not str:
        raise TypeError("text must be a string")
    for c in text:
        if c == '.' or c == '?' or c == ':':
            print(c, "\n")
        else:
            print(c, end="")
