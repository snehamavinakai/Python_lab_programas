#20. Write a python program to demonstrate exception handling

try:
    x =int(input("Enter a number :: "))
    y = (10/x)
    print("Result", y)

except ValueError:
    print("Invalid input please enter a valid input number")

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Eception handling example completed")