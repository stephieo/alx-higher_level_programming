#!/usr/bin/python3
def uppercase(str):
    newstr = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            letter = ord(i)
            i = chr(ord(i) - 32)
            newstr += i
        else:
            newstr += i
            continue
    print("{}".format(newstr))
