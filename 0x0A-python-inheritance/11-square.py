#!/usr/bin/python3
"""Module defining the Square class."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, which is a special case of a rectangle."""

    def __init__(self, size):
        """Initialize a square instance."""
        super().__init__(size, size)

    def __str__(self):
        """Return the square description."""
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)

    def __repr__(self):
        """Return a string representation of the square."""
        return self.__str__()
