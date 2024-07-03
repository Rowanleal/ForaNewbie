import numpy as np 
import matplotlib.pyplot as plt
import math

# numbers=[1,2,3,4,5]
# print(numbers)

# string= str("hello everyone")
# print(string)
# sussy=[]
# for i in range(0,121):
#     sussy.append(i)
# print(sussy)

# ryan_and_olivia = True

# ray = 12

# if ray != 1:
#     print(bool(ray))

# print(f"what is the value of ray: {ray}")

# while ryan_and_olivia and ray <= 10:
#     print(ray)
#     ray = ray + 1
#     print(ray)
#     print('freakybob')


# quadratic formula program

# ask the user for the coefficient values 
a = float(input("Enter the coefficient for the a variable: "))
b = float(input("Enter the coefficient for the b variable: "))
c = float(input("Enter the coefficient for the c variable: "))

# calculate discriminant 
discriminant = b**2 - 4*a*c


# if conditional
# check if discriminant is positive or negative
if discriminant >= 0:
    root1 = (-b + math.sqrt(discriminant))/ (2*a)
    root2 = (-b - math.sqrt(discriminant))/ (2*a)
    print(f"the roots of the equation are {root1} and {root2}")
else:
    print("the equation has no real roots")
