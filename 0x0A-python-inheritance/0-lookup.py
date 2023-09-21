#!/usr/bin/python3
# function that returns list of available attributes and methods of an object


def lookup(obj):
    """Returns list of available attributes and methods of an object."""
    # empty list
    available_att = []

    # check the attributes and store in a variable
    list_of_att = dir(obj)

    # add the variable in the empty list
    available_att.extend(list_of_att)

    # return the list
    return available_att
