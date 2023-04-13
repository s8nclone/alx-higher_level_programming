#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Inverts the int operators == and !=."""

    def __eq__(self, value):
        """Overrides the == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Overrides the != operator with == behavior."""
        return self.real == value
