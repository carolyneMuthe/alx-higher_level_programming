#!/usr/bin/python3
def uppercase(str):
    for char in str:
        # Check if the character is in lowercase
        if ord('a') <= ord(char) <= ord('z'):
            # Convert it to uppercase
            char = chr(ord(char) - 32)
        # Print the character without a newline after each character
        print("{}".format(char), end="")
    # The newline should be added here, after the loop finishes
    print("")
