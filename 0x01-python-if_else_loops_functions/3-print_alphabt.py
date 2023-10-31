#!/usr/bin/python3
for value in range(ord('a'), ord('z') + 1):
    if value == ord('e') or value == ord('q'):
        value = value + 1
        continue
    print("{}".format(chr(value)), end="")
