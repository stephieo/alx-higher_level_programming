#!/usr/bin/python3

print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer
no_c = __import__('5-no_c').no_c
print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer
max_integer = __import__('9-max_integer').max_integer
delete_at = __import__('11-delete_at').delete_at

x = "chicago"
print(no_c(x))
listA = [2, 3, 4, 5, 6]


matrix = [
    [3, 5, 7],
    [9, 11, 13],
    [15, 17, 19]
]
print_matrix_integer(matrix)
print('--')
print_matrix_integer()
print("max: {}".format(max_integer(listA)))
print_reversed_list_integer(listA)
idx = 3
new_list = delete_at(listA, idx)
print(new_list)