#6. Write a python program to Check if a number is Odd or Even

num = int(input("Enetr a number to check whether its even or odd : "))

if num % 2 == 0:
    result = "Even"
else:
    result = "Odd"

print(f'The number {num} is {result}.')