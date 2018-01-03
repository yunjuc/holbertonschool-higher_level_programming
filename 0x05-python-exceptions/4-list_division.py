#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    try:
#         for x, y in list(zip(my_list_1, my_list_2)):
#                new[i] = x / y
        for i in range(list_length):
            new.append(my_list_1[i] / my_list_2[i])
    except TypeError:
        print("wrong type")
    except ZeroDivisionError:
        print("division by 0")
    except IndexError:
        print("out of range")
    finally:
        return new
