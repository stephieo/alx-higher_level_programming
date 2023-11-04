#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    blist = my_list.copy()
    for i, item in enumerate(my_list):
        if item % 2 != 0:
            blist[i] = False
        else:
            blist[i] = True
    return blist
