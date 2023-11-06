#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        return
    else:
        for row in matrix:
            for item in row:
                if row.index(item) < (len(row) - 1):
                    print("{:d}, ".format(item), end="")
                else:
                    print("{:d}".format(item), end="")
            print()
