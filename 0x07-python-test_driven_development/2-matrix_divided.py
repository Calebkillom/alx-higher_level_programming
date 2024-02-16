#!/usr/bin/python3
""" function that divides all elements of a matrix. """


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
        matrix (list): A list of lists containing integers or floats.
        div (int/float): The divisor.

    Returns:
        list: A new matrix with elements divided by the divisor,
              rounded to 2 decimal places.

    Raises:
        TypeError: If div is not a number or if matrix is not a matrix
                   (list of lists) of integers/floats, or if any element
                   of the matrix is not an integer or float.
        ZeroDivisionError: If div is 0.
        TypeError: If each row of the matrix doesn't have the same size.
    """
    try:
        if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")
        elif div == 0:
            raise ZeroDivisionError("division by zero")

        if (not isinstance(matrix, list)) or \
                (not all(isinstance(row, list) for row in matrix)):
            raise TypeError("matrix must be a matrix (list of lists)"
                            "of integers/floats")

        for row in range(len(matrix)):
            if len(matrix[row]) != len(matrix[0]):
                raise TypeError("Each row of the matrix"
                                " must have the same size")

        new_matrix = []

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
    except Exception as e:
        raise e
