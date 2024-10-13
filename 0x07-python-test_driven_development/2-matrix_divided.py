#!/usr/bin/python3
"""
This module provides a function to divide all elements
of a matrix by a divisor.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of the matrix by div and returns a new matrix.

    Args:
        matrix (list of lists): A list of lists where each inner list contains 
                                integers or floats.
        div (int/float): The divisor, must be a non-zero integer or float.

    Returns:
        A new matrix where each element is divided by div, rounded to 2 
        decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats, 
                   or if rows are not the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.
    """

    # Check if matrix is a list of lists containing integers or floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) 
                                               for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/"
                        "floats")
    if not all(isinstance(el, (int, float)) for row in matrix for el in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/"
                        "floats")
    
    # Check if all rows in the matrix are of the same size
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div and round to 2 decimal places
    return [[round(el / div, 2) for el in row] for row in matrix]
