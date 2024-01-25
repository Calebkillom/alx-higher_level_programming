#!/usr/bin/python3
""" function that returns the number of keys in a dictionary """


def number_keys(a_dictionary):
    """ returns the number of keys in a dictionary """
    total = 0

    for k, v in a_dictionary.items():
        total = total + 1

    return total
