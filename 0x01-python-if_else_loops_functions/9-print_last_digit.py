#!/usr/bin/python3
def print_last_digit(number):
    '''print the last digit of a number'''
    if number < 0:
        number = -1 * number
    number = number % 10
    print(number, end="")
    return number
