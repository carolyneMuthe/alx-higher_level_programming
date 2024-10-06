#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Use only the first two elements or default to 0 if missing
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0
    b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0
    
    # Return a tuple with the sums of the first and second elements
    return (a1 + b1, a2 + b2)
