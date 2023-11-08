def square_matrix_simple(matrix=[]):
    lambda: i ** i
    output = []
    for j in matrix:
        output.append(list(map(lambda i: i ** i, matrix)))
    print(output)

test = [[2, 3, 4] , [2, 8, 9], [0, 5, 6]]
square_matrix_simple(test)
