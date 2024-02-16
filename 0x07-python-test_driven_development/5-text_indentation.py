#!/usr/bin/python3
""" function that prints a text with 2 new lines """


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text to be processed.

    Raises:
        TypeError: If the input `text` is not a string.
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Define characters that trigger new lines
    trigger_characters = ['.', '?', ':']

    # Initialize an empty result string
    result = ""

    # Iterate over each character in the text
    for char in text:
        # Add the character to the result string
        result += char

        # If the character is a trigger character, add two new lines
        if char in trigger_characters:
            result += "\n\n"

    # Print the result without leading or trailing spaces
    print('\n'.join(line.strip() for line in result.split('\n')))
