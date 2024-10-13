#!/usr/bin/python3
"""
This module provides a function to divide all elements
of a matrix by a divisor.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given number.

    Args:
        matrix: A list of lists of integers or floats.
        div: A number (integer or float) to divide the matrix elements by.

    Returns:
        A new matrix with the divided values, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.
    """
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all
    (isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix(list of lists)
                                                   of integers/floats")

    # Check if all rows have the same size
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if all elements are integers or floats
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float))
                raise TypeError("matrix must be a matrix(list of lists)
                                                                of integers/floats")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Create a new matrix with the divided values
    return [[round(element / div, 2) for element in row] for row in matrix]
