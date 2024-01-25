#!/usr/bin/python3
""" function that computes the square value of all integers of a matrix """


def square_matrix_simple(matrix=[]):
    """ computes the square value of all integers """
    sqmat = [[element**2 for element in row] for row in matrix]
    return sqmat
