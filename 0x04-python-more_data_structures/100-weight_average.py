#!/usr/bin/python3
""" returns the weighted average of all integers tuple """


def weight_average(my_list=[]):
    """Calculates the weighted average of integers in tuples"""
    if not my_list:
        return 0

    total_score = 0
    total_weight = 0

    for score, weight in my_list:
        total_score += score * weight
        total_weight += weight

    if total_weight == 0:
        return 0

    return total_score / total_weight
