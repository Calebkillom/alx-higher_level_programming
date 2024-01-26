#!/usr/bin/python3
""" returns list with all values multiplied by a number"""


def multiply_list_map(my_list=[], number=0):
    """Returns a new list with all values multiplied using map """
    return list(map(lambda element: element * number, my_list))
