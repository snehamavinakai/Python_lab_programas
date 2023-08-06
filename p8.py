#8. Write a python to find the factorial of a number

num = int(input("Enter a number : "))
fact = 1

if num < 0:
    print("Factorial is not defined for negative numbers")

elif num == 0:
    print("The factorial of 0 is 1")

else:
    for i in range (1, num+1):
        fact *=i
    print(f'The factorial of {num} is {fact}' )