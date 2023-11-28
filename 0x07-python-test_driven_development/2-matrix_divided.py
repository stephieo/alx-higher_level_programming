#!/usr/bin/python3
""" this module contains a function that divides all elements in a matrix"""


def matrix_divided(matrix, div):
    """ this function divides all elements in a matrix

    Args:
        matrix (list): must be a 2-d list
        div (int): second parameter. must be a valid number

    Returns:
        a new matrix with the quotient of each element

    Raises:
        TypeError: if matrix is not a list of
            lists or elements are not int or float
        TypeError: if matrix rows are unequal
        TypeError: if div is not int or float
        ZeroDivisionError: if div is 0
    """
    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    elif not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    elif not all(isinstance(elem, (int, float))
                 for row in matrix for elem in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    control = matrix[0]
    for row in matrix:
        if len(control) != len(row):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        sub_list = []
        for elem in row:
            sub_list.append(round(elem / div, 2))
        new_matrix.append(sub_list)

    return new_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
