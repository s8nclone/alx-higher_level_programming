#!/usr/bin/python3
for num in range(0, 99):
    if num == 99:
        print("{:d}".format(num))
    else:
        print("{0:02d}".format(num), end=", ")
