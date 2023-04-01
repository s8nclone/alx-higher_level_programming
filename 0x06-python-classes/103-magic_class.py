#!/usr/bin/python3
"""Define a magic class that does exatly as the bytecode provided."""


import math


class MagicClass:
    """Represents a circle."""

    def __init__(self, radius=0):
        """Initializes a magic class.

        Args:
            radius (float or int): The radius of the new magic class.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the magic class."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return the circumference of the magic class."""
        return (2 * math.pi * self.___radius)
