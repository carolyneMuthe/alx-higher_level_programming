#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # Check if the key exists in the dictionary
    if key in a_dictionary:
        # If it exists, delete it
        del a_dictionary[key]
    # Return the updated dictionary
    return a_dictionary
