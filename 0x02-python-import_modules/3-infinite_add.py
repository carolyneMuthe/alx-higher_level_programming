#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  # Exclude the script name
    result = sum(int(arg) for arg in argv)  # Convert arguments to integers and sum them
    print(result)
