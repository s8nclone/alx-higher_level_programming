#!/usr/bin/python3
"""
write_file function module.

Defines a write_file function.
"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8).
    and returns the number of characters written.

    filename: file, create if nonexist, must have permissions.
    text: text, overwites contents of files if already exists.
    """
    with open(filename, mode="w", encoding="UTF-8") as my_file:
        return my_file.write(text)
