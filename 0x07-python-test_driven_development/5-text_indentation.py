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
    text = text.strip()
    flag = False
    for c in text:
        if c == ' ' and flag == True:
            continue
            flag = False
        if c in ['.', '?', ':']:
            print(c)
            print()
            flag = True
        else:
           print(c, end="")
           flag = False
