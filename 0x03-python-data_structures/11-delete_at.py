#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Check if the index is valid
    if idx < 0 or idx >= len(my_list):
        return my_list  # Return the list unchanged

    # Create a new list to store elements except the one at idx
    new_list = []

    # Iterate over the original list and build the new list
    for i in range(len(my_list)):
        if i != idx:
            new_list.append(my_list[i])

    return new_list
