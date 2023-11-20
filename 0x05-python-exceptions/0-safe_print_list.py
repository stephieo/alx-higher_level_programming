#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    print_count = 0
    try:
        for i in my_list:
            print("{:d}".format(i), end="")
            print_count += 1
    except IndexError as e:
         return print_count
    print()

    return print_count

list1 =[ 1,4, 5, 6, 9]
safe_print_list(list1, 3)