#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, mul, div, sub

    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operators = ["+", "-", "/", "*"]
    functions = [add, sub, div, mul]

    if argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        op = operators.index(argv[2])

        print("{:d} {} {:d} = {}".format(a, argv[2], b, functions[op](a, b)))
