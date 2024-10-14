#!/usr/bin/python3
"""
0-add_integer - A module for adding two integers.

This module contains the function add_integer which adds two integers
or floats and returns the result as an integer.
"""


def add_integer(a, b=98):
    """
    add_integer - Adds two integers.

    Args:
        a (int, float): The first integer.
        b (int, float, optional): The second integer. Defaults to 98.

    Raises:
        TypeError: If a is not an integer or float,
        or if b is not an integer or float.

    Returns:
        int: The sum of a and b as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
