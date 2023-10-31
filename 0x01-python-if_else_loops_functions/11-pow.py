#!/usr/bin/python3
def pow(a, b):
    if a > 0 and b < 0:
        result = 1 / (a ** (-b))
    elif a < 0 and b > 0:
        sign = -1 ** b
        result = ((-a) ** b) * sign
    else:
        result = a ** b

    return abs(result)
