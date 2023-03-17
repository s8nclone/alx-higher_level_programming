#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return (0)
    roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    num = 0
    dictr = [roman_dict[x] for x in roman_string]
    for i in range(len(dictr)):
        num += dictr[i]
        if dictr[i - 1] < dictr[i] and i != 0:
            num -= (dictr[i - 1] + dictr[i - 1])
    return num
