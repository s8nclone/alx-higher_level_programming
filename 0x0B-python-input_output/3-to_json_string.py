#!/usr/bin/python3
"""Defines a to_json_string function"""

import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object(string).

    my_obj: object to dump into JSON.
    """
    return json.dumps(my_obj)
