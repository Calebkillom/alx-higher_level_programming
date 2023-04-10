#!/usr/bin/python3

def matrix_divided(matrix, div):
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    # Check if matrix is a list of lists
    if (not isinstance(matrix, list)) or \
            (not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists)"
                        "of integers/floats")

    # Check if all rows have the same length
    for row in range(len(matrix)):
        if len(matrix[row]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []

    # Perform division on each element in the matrix
    for row in range(len(matrix)):
        new_row = []
        for col in range(len(matrix[row])):
            element = matrix[row][col]
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)"
                                "of integers/floats")
            else:
                element = round(element / div, 2)
                new_row.append(element)
        new_matrix.append(new_row)

    return new_matrix
