#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("{:d} arguments.".format(len(argv) - 1))
    if len(argv) == 2:
        print("{:d} argument:\n{:d}: {}".format(len(argv) - 1, len(argv) - 1, argv[1]))
    if len(argv) > 2:
        print("{:d} arguments:".format(len(argv) - 1))
        for i in range(1, len(argv)):
            print("{:d}: {}".format(i, argv[i]))
"""
    if len(argv) > 1:
        print("{:d} arguments:".format(len(argv)))
        for i, arg in enumerate(argv, start=1):
            print("{:d}: {}".format(i, arg))
        elif len(argv) == 1:
            print("{:d} argument:\n{:d}: {}".format(len(argv), len(argv), argv[1]))
        else:
            print("0 arguments.")
            """
