#!/usr/bin/python3
"""Defines a class square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new square.

        Args:
            size: The size of a new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return current area of the square."""
        return (self.__size * self.__size)
