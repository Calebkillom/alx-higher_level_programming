#!/usr/bin/python3
""" Check if obj is an instance of a subclass of a_class """


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of
    or if the object is an instance of a class
    that inherited from, the specified class; otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    for subclass in obj.__class__.mro()[1:]:
        if subclass == a_class:
            return True
    return False