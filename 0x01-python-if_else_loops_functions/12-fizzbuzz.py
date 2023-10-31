#!/usr/bin/python3

 def fizzbuzz():
    for i in range(1, 101):
        if (i % 3) == 0:
            print("fizz", end=" ") 
        elif (i % 5) == 0 and i != 100:
            print("buzz", end=" ") 
        elif i == 100:
            print("buzz")
        else:
            print(i, end=" ")
