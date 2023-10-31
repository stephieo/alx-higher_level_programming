#!/usr/bin/python3

def remove_char_at(str, n):
    if n != -1:
        copy = str[: n] + str[(n+1) :]
    else:
        copy = str[:-1]
    print(copy)