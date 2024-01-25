#!/usr/bin/python3
""" function that adds all unique integers in a list """


def uniq_add(my_list=[]):
    """ adds all unique integers in a list (only once for each integer) """
    uniqnumb = set()
    total = 0

    for num in my_list:
        if num not in uniqnumb:
            total += num
            uniqnumb.add(num)

    return total
