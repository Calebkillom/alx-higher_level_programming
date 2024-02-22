#!/usr/bin/python3
"""Check if obj is an instance of a subclass of a_class"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of
    a class that inherited (directly or indirectly)
    from the specified class; otherwise False.
    """
    for subclass in obj.__class__.mro()[1:]:
        if subclass == a_class:
            return True
    return False
