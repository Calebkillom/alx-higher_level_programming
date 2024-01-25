#!/usr/bin/python3
""" function that prints a dictionary by ordered keys """


def print_sorted_dictionary(a_dictionary):
    """ prints a dictionary by ordered keys """
    for key in sorted(a_dictionary.keys()):
        value = a_dictionary[key]
        print(f"{key}: {value}")
