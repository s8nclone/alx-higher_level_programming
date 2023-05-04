#!/usr/bin/python3
import json


"""Defines a save-to_json_file function."""


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON representation.

    my_obj: object
    filename: file to write to
    """
    with open(filename, 'w', encoding='UTF-8') as my_file:
        my_file.write(json.dumps(my_obj))
