#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            return True
        print("{} is divisible by 2".format(my_list(i)))
        else:
            return False
        print("{} is  not divisible by 2".format(my_list(i)))
