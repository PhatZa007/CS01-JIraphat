def greet():
    print("Hello world!")

#call the function
greet()

print("Outside function")
print("_____________________________________")

def plus(num1 , num2):
    sum = num1 + num2
    print("Sum: ", sum)
plus(5 , 4)
print("_____________________________________")

def fs(num):
    result = num * num
    return result
square = fs(3)
print("Square:" , square)
print("_____________________________________")

def plu(num4 , num5):
    result = num4 + num5
    return result
plus = plu(5 , 4)
print("Sum:" , plus)
print("_____________________________________")

import math
square_root = math.sqrt(4)
print("Square Root of 4 is" , square_root)
power = pow(2 , 3)
print("2 to the power of 3 is" , power)
print("_____________________________________")