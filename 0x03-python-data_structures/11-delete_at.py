#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Check if the index is valid
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
