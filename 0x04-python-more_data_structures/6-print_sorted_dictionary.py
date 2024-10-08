#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Sort the keys of the dictionary and iterate through them
    for key in sorted(a_dictionary):
        # Print each key and its corresponding value
        print(f"{key}: {a_dictionary[key]}")
