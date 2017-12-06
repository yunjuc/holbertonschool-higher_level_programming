#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {:d} is ".format(number), end="")
if number < 0:
    last_digit = abs(number) % 10 * -1
else:
    last_digit = number % 10
if 0 < last_digit < 6:
    print("{:d} and is less than 6 and not 0".format(last_digit))
elif last_digit == 0:
    print("{:d} and is 0".format(last_digit))
else:
    print("{:d} and is greater than 5".format(last_digit))
