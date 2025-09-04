#!/usr/bin/python3
"""Defines a Square with print method."""


class Square:
    """Square class with size validation, area and print method."""

    def __init__(self, size=0):
        """Initialize square with optional size."""
        self.size = size

    @property
    def size(self):
        """Retrieve size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with #, or empty line if size == 0."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
