#!/usr/bin/python3
def print_last_digit(number):
    # Get the last digit by using abs() to handle negative numbers
    last_digit = abs(number) % 10
    # Print the last digit
    print(last_digit, end="")
    return last_digit
