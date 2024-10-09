#!/usr/bin/python3
"""
This module defines a Square class that represents a square.
"""


class Square:
    """
    This class defines a square with a specific size.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square.

        Args:
            size (int, float, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not a number (int or float).
            ValueError: If size is less than 0.
        """
        self.size = size  # Use the setter to set the size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int, float): The new size value.

        Raises:
            TypeError: If size is not a number (int or float).
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value  # Set the private attribute

    def area(self):
        """Return the current square area."""
        return self.size ** 2

    # Comparison methods based on area
    def __eq__(self, other):
        """Return True if areas are equal."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Return True if areas are not equal."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Return True if this square is less than the other."""
        return self.area() < other.area()

    def __le__(self, other):
        """Return True if this square is less than or equal to the other."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Return True if this square is greater than the other."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Return True if this square is greater than or equal to the other."""
        return self.area() >= other.area()
