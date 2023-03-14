#!/usr/bin/python3
"""Print all possible different combinations of two digits in ascending order.

    The two digits must be different -  01 and 10 are considered the same.
    """

for num1 in range(0, 9):
    for num2 in range(num1 + 1, 10):
        if num1 == 8 and num2 == 9:
            print("{:d}{:d}".format(num1, num2))
        else:
            print("{:d}{:d}".format(num1, num2), end=", ")
