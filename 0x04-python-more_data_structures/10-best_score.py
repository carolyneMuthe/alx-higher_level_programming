#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    # Use max function to find the key with the largest value
    return max(a_dictionary, key=a_dictionary.get)
