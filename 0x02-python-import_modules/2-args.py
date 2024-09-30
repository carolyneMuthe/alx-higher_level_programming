#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    arg_count = len(argv)

    # Print the number of arguments
    if arg_count == 0:
        print("0 arguments.")
    elif arg_count == 1:
        print("1 argument:")
    else:
        print(f"{arg_count} arguments:")

    # Print each argument with its position
    for i, arg in enumerate(argv, 1):
        print(f"{i}: {arg}")
