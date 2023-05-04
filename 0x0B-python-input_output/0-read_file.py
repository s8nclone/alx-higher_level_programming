#!/usr/bin/python3
"""
read_file function module.

Defines a read_file function.
"""


def read_file(filename=""):
    """Reads a text file(UTF8) and prints it to stdout.

    filename (file):
    """
    with open(filename, encoding="UTF-8") as my_file:
        print(my_file.read(), end="")
