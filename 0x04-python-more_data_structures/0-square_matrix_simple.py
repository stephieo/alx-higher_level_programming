#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    output = []
    for j in matrix:
        output.append(list(map(lambda i: i ** 2, j)))
    return output
