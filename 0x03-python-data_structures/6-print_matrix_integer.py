#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, element in enumerate(row):
            if i != 0:
                print(" ", end="")
            print("{:d}".format(element), end="")
        print()  # Move to the next line after printing each row
