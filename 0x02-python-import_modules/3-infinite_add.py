#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv
    add = 0
    for arg in range(len(args) - 1):
        add += int(args[i + 1])
        print("{:d}".format(add))
