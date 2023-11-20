#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    print_count = 0
    try:
        for i in range(x):
            print("{:d}".format(i), end="")
            print_count += 1
    except IndexError as e:
        break
    print()

    return print_count
