#4. Write a python program to swap two variable

num1 = float(input("Enetr the first number : "))
num2 = float(input("Enetr the second number : "))

print("Before Swapping : ")
print("First number : ", num1)
print("Second number : ", num2)

num1, num2 = num2, num1

print("After Swapping : ")
print("First number : ", num1)
print("Second number : ", num2)