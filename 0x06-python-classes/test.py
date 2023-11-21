#!/usr/bin/python3
Square = __import__('2-square').Square

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
    
my_square = Square()
print(type(my_square))
print(my_square.__dict__)
