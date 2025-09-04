#!/usr/bin/python3
"""Defines a Square with size validation and area."""


class Square:
    """Square class with private size and area method."""

    def __init__(self, size=0):
        """Initialize square and validate size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return area of the square."""
        return self.__size **
