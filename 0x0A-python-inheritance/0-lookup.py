#!/usr/bin/python3
"""
function that returns list of available attributes and methods of an object
"""


def lookup(obj):
    """Returns list of available attributes and methods of an object."""
    return dir(obj)
