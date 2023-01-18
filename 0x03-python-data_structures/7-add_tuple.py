#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    size1 = len(tuple_a)
    size2 = len(tuple_b)

    # convert tuple to list using list()
    # convert list to tuple using tuple()
    if size1 < 2:
        list_a = list(tuple_a)
        while len(list_a) < 2:
            list_a.append(0)
        tuple_a = tuple(list_a)

    if size2 < 2:
        list_b = list(tuple_b)
        while len(list_b) < 2:
            list_b.append(0)
        tuple_b = tuple(list_b)

    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return new_tuple
