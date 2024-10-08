#!/usr/bin/python3

def safe_print_integer(value):
    try:
        # Attempt to print the value using the specified format
        print("{:d}".format(value))
        return True  # Return True if the print is successful
    except (ValueError, TypeError):
        return False  # Return False if an exception occurs
