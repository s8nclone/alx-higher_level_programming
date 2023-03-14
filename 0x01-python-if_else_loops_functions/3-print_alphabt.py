#!/usr/bin/python3
for i in (97, 123):
    if chr(i) == 'e' or chr(i) == 'q':
        continue
    print(chr(i).format(i), end='')
