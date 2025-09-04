#!/usr/bin/python3
"""Defines a Square with a private size."""


class Square:
    """Square class with private attribute size."""

    def __init__(self, size):
        """Initialize square with size (no checks)."""
        self.__size = size
