#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    """Print an integer or handle the exception."""
    try:
        # Attempt to print the value formatted as an integer
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        # Print the error message to stderr
        print("Exception: {}".format(e), file=sys.stderr)
        return False
