#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Counter for the number of integers printed
    i = 0  # Initialize the index for iteration

    while i < x:
        try:
            # Try to access the element at index i
            value = my_list[i]
            # Check if the value is an integer
            if isinstance(value, int):
                print("{:d}".format(value), end="")
                count += 1  # Increment the count for each integer printed
        except IndexError:
            # If an IndexError occurs, print a newline and raise the exception
            print()  # Ensure a newline before raising the exception
            raise  # Re-raise the exception to show the traceback
        i += 1  # Move to the next index

    print()  # Ensure a newline after printing all integers
    return count  # Return the number of integers printed
