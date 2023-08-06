#7. Write a python program to Print all prime Number in an interval

start = int(input("Enter the starting number of the interval : "))
end = int(input("Enter the ending number of the interval : "))

print(f'Prime numbers between {start} and {end} are : ')

for num in range(start, end+1):
    if num > 1:
        is_prime = True
        for i in range (2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)