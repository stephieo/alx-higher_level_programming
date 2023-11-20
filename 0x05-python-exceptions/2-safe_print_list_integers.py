#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    print_count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            print_count += 1
        except ValueError:
            continue
    print()
    return print_count

list2 = [2, 3, 9, 5, ]
print(safe_print_list_integers(list2, 56))
