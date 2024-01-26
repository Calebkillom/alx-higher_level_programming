#!/usr/bin/python3
"""converts a Roman numeral to an integer """


def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer."""
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0

    for i in range(len(roman_string) - 1):
        current_value = roman_numerals[roman_string[i]]
        next_value = roman_numerals[roman_string[i + 1]]

        if current_value < next_value:
            result -= current_value
        else:
            result += current_value

    result += roman_numerals[roman_string[-1]]
    return result
