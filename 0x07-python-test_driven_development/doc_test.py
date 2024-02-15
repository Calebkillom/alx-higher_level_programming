#!/usr/bin/python3
# Module docstring
"""
This module provides various mathematical functions.
"""

# Function with docstring
def add(x, y):
    """
    Add two numbers together.

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        int: The sum of x and y.
    """
    return x + y

# Special __test__ attribute
__test__ = {
    'multiply': lambda x, y: x * y,
    'division': 'Perform division operation',
}

# Class with docstring
class Calculator:
    """
    A simple calculator class.
    """

    def subtract(self, x, y):
        """
        Subtract two numbers.

        Args:
            x (int): The first number.
            y (int): The second number.

        Returns:
            int: The difference between x and y.
        """
        return x - y
