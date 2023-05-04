#!/usr/bin/python3
"""Defines a class_to_json function"""


def class_to_json(obj):
    """Returns the dictionary description with simple data
    structure for JSON serialization of an object.

    obj: instance of a class
    """
    return obj.__dict__
