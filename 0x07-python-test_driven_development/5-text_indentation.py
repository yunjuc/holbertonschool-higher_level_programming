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
    i = 0
    while i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i], "\n")
            i += 2
        else:
            print(text[i], end="")
            i += 1
