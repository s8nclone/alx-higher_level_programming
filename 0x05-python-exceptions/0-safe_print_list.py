#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    num = 0
    while True:
        try:
            if num < x:
                print(my_list[num], end="")
                num += 1
            else:
                print()
                return num
        except IndexError:
            print()
            return num
