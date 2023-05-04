#!/usr/bin/python3
"""
append_write function module.

Defines a append_write function.
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8).
    and returns the number of characters added.

    filename: file, create if nonexist, must have the required permissions.
    text: text, append at the end.
    """
    with open(filename, mode='a', encoding='UTF-8') as my_file:
        return my_file.write(text)
