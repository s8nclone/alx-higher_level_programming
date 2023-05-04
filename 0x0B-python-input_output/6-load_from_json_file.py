#!/usr/bin/python3
"""Defines a load_from_json_file function"""

import json


def load_from_json_file(filename):
    """Creates an object from a "JSON file".

    filename: file
    """
    with open(filename, 'r', encoding='UTF-8') as my_file:
        return json.loads(my_file.read())
