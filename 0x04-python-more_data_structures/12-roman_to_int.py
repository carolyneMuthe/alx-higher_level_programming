#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    # Dictionary to map Roman numerals to their integer values
    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev_value = 0

    # Iterate over the Roman numeral string in reverse
    for char in reversed(roman_string):
        value = roman_numerals.get(char, 0)

        if value >= prev_value:
            total += value  # Add if current value is greater or equal
        else:
            total -= value  # Subtract if current value is less

        prev_value = value

    return total
