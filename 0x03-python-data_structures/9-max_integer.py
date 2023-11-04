#!/usr/bin/python3
def max_integer(my_list=[]):
    last_num = len(my_list) - 1
    if not my_list:
        return
    else:
        for i in range(len(my_list)):
            if i < last_num:
                if my_list[i] > my_list[i + 1]:
                    max = my_list[i]
            elif i == last_num:
                if my_list[i] > my_list[i - 1]:
                    max = my_list[i]
    return max
