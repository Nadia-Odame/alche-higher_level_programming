#!/usr/bin/python3
"""
This module defines a Square class.
The class validates size and can compute the area of the square.
"""


class Square:
    """
    Represents a square with size validation and area calculation.
    """

    def __init__(self, size=0):
        """
        Initialize the square.

        Args:
            size (int): The size of the square (default 0).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Return the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
