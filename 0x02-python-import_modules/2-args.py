#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

print("{:d}".format(len(argv) - 1), end="")
if (len(argv) - 1) == 0:
    print(" arguments.")
elif (len(argv) - 1) == 1:
    print(" argument:")
    print("{:d}: {}".format(1, argv[1]))
elif (len(argv) - 1) > 0:
    print(" arguments:")
    for i in range(len(argv) - 1):
        print("{:d}: {}".format(i + 1, argv[i + 1]))
