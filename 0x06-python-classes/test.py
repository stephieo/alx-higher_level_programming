#!/usr/bin/python3
Square = __import__('101-square').Square

try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)

try:
    my_square_3 = Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)
    
my_square = Square(3, (6,2))
print("Area: {} for size: {}".format(my_square.area(), my_square.size))
my_square.my_print()
print("---using __str__:")
print(my_square)
print("--")

mysquare = Square(5) 
mysquare.my_print()
try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)
