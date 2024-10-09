#!/usr/bin/python3
# 1-square.py
# A class that defines a square by its size.

class Square:
    """Class that defines a square."""
    
    def __init__(self, size):
        """Initialize a new square.
        
        Args:
            size (int): The size of the square.
        """
        self.__size = size  # Private attribute
