#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
        return result
    except ZeroDivisionError as e:
        result = None
        return
    finally:
        print("Inside result: {}".format(result))
