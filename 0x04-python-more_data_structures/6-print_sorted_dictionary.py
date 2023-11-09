#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted(a_dictionary)
    in_order = a_dictionary.items()
    for key, value in in_order:
        print("{}: {}".format(key, value))
    return in_order
