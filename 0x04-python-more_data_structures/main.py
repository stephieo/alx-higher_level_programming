#!/usr/bin/python3

square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple
search_replace = __import__('1-search_replace').search_replace
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(square_matrix_simple(matrix))
