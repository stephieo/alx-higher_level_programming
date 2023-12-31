#!/usr/bin/python3

square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple
search_replace = __import__('1-search_replace').search_replace
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary
update_dictionary = __import__('7-update_dictionary').update_dictionary
simple_delete = __import__('8-simple_delete').simple_delete
multiply_by_2 = __import__('9-multiply_by_2').multiply_by_2
best_score = __import__('10-best_score').best_score
multiply_list_map = __import__('11-multiply_list_map').multiply_list_map

my_list = [1, 2, 3, 4, 6]
new_list = multiply_list_map(my_list, 4)
print(new_list)
print(my_list)

a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

new_dict = multiply_by_2(a_dictionary)
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)


a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3] }
new_dict = simple_delete(a_dictionary, 'track')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

print("--")

test= {}
dir(test)
a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
new_dict = update_dictionary(a_dictionary, 'name', "Monty")
print_sorted_dictionary(new_dict)
print("--")

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
my_dict = { 'a': "a", 'b': "b" , 'c': "c", 'd': "d", 'e': "e" }
print_sorted_dictionary(a_dictionary)
print_sorted_dictionary(my_dict)

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
