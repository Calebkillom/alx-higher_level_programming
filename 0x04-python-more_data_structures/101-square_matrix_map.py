#!/usr/bin/python3
""" Computes square value of all integers of a matrix using map """


def square_matrix_map(matrix=[]):
    """Computes the square value of all integers in a matrix using map"""
    return list(map(lambda row: list(map(lambda x: x**2, row)), matrix))
