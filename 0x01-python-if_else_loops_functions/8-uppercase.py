#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            up_str = chr(ord(i) - ord('a') + ord('A'))
        else:
            up_str = i
            print('{}{}'.format(up_str, ''), end='')
        print('')
