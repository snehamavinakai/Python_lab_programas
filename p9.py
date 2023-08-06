#9. Write a python program to Display the multiplication Table

num = int(input("Enter a number : "))

print(f'Multiplication table for {num} is :')

for i in range(1,11):
    res = num * i
    print(f'{num} * {i} = {res}')