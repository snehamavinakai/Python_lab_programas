#3. Write a python program to solve quadratic equation

import cmath

a = float(input("Enter the co-efficient a : "))
b = float(input("Enter the co-efficient b : "))
c = float(input("Enter the co-efficient c : "))

discriminant = (b**2) - (4*a*c)

solution1 = (- b + cmath.sqrt(discriminant))/(2*a)

solution2 = (- b - cmath.sqrt(discriminant))/(2*a)

print("The solutions are : ")
print("x1 = ", solution1)
print("x2 = ", solution2)