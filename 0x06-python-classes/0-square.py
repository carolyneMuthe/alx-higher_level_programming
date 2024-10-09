#!/usr/bin/python3
"""
This module defines a Square class with a private attribute size.
"""

class Square:
    """A class that defines a square by its size."""
    
    def __init__(self, size):
        """Initialize a new square with the given size.
        
        Args:
            size (int): The size of the square.
        """
        self.__size = size  # Private instance attribute
