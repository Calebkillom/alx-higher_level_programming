#!/usr/bin/python3
""" function that deletes a key in a dictionary """


def simple_delete(a_dictionary, key=""):
    """Deletes a key from a dictionary if it exists"""
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary