#!/usr/bin/python3
import json


"""Defines a from_json_string function"""


def from_json_string(my_str):
    """Returns an object represented by a JSON string.

    my_str: string to load from JSON.
    """
    return json.loads(my_str)
