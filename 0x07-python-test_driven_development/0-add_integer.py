#!/usr/bin/python3
"""
This module provides a function add_integer
that adds two integers or floats.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the sum.
    If a or b are floats, they are cast to integers.
    Raises:
        TypeError: if a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast floats to integers
    a = int(a)
    b = int(b)
    
    return a + b