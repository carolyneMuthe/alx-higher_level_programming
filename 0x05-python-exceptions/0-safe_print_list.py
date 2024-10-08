#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0  # Counter for the number of elements printed
    for i in range(x):
        try:
            print(my_list[i], end='')  # Print each element without a new line
            count += 1  # Increment the counter for each successfully printed element
        except IndexError:
            break  # Exit the loop if we reach an index that doesn't exist
    print()  # Print a new line after printing the elements
    return count  # Return the number of elements printed
