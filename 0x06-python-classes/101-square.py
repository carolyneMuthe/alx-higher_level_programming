#!/usr/bin/python3
"""
This module defines a Square class that represents a square.
"""


class Square:
    """
    This class defines a square with a specific size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square.
                Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or if position is not a tuple
                of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size  # Use the setter to set the size
        self.position = position  # Use the setter to set the position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value  # Set the private attribute

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value (tuple): The new position value.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value  # Set the private attribute

    def area(self):
        """Return the current square area."""
        return self.size ** 2

    def my_print(self):
        """Print the square using the character #."""
        if self.size == 0:
            print("")  # Print an empty line if size is 0
            return

        # Print the position (leading spaces)
        for _ in range(self.position[1]):
            print("")  # Print empty lines for the vertical position
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        """Return the string representation of the square."""
        square_str = ""
        if self.size == 0:
            return square_str  # Return empty string for size 0
        for _ in range(self.position[1]):
            square_str += "\n"  # Add empty lines for vertical position
        for _ in range(self.size):
            square_str += " " * self.position[0] + "#" * self.size + "\n"
        return square_str[:-1]  # Remove the last newline character
