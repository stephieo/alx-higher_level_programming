#!/usr/bin/python3

def remove_char_at(str, n):
    if n < 0:
        return str
    if n != -1:
        copy = str[: n] + str[(n+1):]
    else:
        copy = str[:-1]
    return copy
