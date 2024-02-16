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
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    trigger_characters = ['.', '?', ':']

    result = ""

    for char in text:
        result += char

        if char in trigger_characters:
            result += "\n\n"

    print('\n'.join(line.strip() for line in result.split('\n')))
