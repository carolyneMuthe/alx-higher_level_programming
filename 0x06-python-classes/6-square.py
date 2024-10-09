#!/usr/bin/python3
"""
This module defines a class Square with private instance attributes size and position.
"""


class Square:
    """
    This class represents a square with private size and position attributes.
    It includes methods to get and set the size and position, calculate the area,
    and print the square using the '#' character.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square. Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or if position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size  # Use the setter to set the size
        self.position = position  # Use the setter to set the position

    @property
    def size(self):
        """
        Retrieve the current size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size of the square.

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
        """
        Retrieve the current position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                any(i < 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value  # Set the private attribute

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2  # Area calculation

    def my_print(self):
        """
        Print the square with the character '#'.

        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print("")  # Print an empty line
            return

        # Print empty lines for the y position
        for _ in range(self.__position[1]):
            print("")  # This accounts for vertical spacing

        # Print the square with the correct horizontal position
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)  # Horizontal spacing and square row

