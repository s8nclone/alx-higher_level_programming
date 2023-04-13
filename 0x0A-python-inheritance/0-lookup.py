#!/usr/bin/python3
"""Defines an object attribute lookup funtion."""


def lookup(obj):
    """Returns a list of available attributes and methods of an onject."""
    return (dir(obj))
