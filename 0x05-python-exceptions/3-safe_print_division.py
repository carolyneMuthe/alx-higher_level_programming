#!/usr/bin/python3

def safe_print_division(a, b):
    """Divides two integers and prints the result."""
    try:
        result = a / b  # Perform division
    except ZeroDivisionError:
        result = None  # If division by zero, set result to None
    finally:
        # Print the result or None if an exception occurred
        print("Inside result: {}".format(result))

    return result  # Return the result of the division
