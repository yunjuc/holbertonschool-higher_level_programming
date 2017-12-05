#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    new = -1 * number
else:
    new = number
last_digit = new % 10
if 0 < last_digit < 6:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, last_digit))
elif last_digit == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, last_digit)) 
else:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, last_digit)) 
