#!/usr/bin/python3
""" function that returns a set of all elements present in only one set """


def only_diff_elements(set_1, set_2):
    """ returns a set of all elements present in only one set """
    a = set(set_1)
    b = set(set_2)
    return a ^ b
