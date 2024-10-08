#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Initialize a counter for the number of integers printed
    for i in range(x):
        try:
            # Check if the element is an integer before trying to print it
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1  # Increment the counter for each integer printed
        except IndexError:
            # Break the loop if IndexError occurs (x exceeds the list length)
            break
    print()  # Print a newline after printing all integers
    return count  # Return the number of integers printed
