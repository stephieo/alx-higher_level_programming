#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = lambda i: i ** i
    output = []
    for j in matrix:
        output.append([square for i in j])
    print(output)

