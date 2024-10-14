#!/usr/bin/python3
class MyList(list):
    """Inherits from list and adds a method to print the list
    sorted in ascending order."""


    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)."""
        print(sorted(self))
