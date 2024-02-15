#!/usr/bin/python3
""" function that adds 2 integers """


def add_integer(a, b=98):
    """ add_integer returns sum of two integers
        Args:
            a (int): first operand
            b (int): second operand

        Returns:
            sum of the two operands
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
