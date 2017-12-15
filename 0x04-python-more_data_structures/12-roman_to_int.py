#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
            'M': 1000}
    total = 0
    for idx, c in enumerate(roman_string):
        total += dict.get(c)
        if idx <= len(roman_string) - 1 and idx != 0:
            if dict.get(roman_string[idx - 1]) < dict.get(c):
                total -= 2 * dict.get(roman_string[idx - 1])
    return total
