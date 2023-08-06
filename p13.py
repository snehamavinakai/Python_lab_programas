#13. Write a python program to input an array of n numbers and find separately the sum of positive and negative numbers

list_item = []

def main():
    n = int(input("Enter the number of values to be inserted : "))
    
    for i in range(n):
        num = int(input("Enter a number :: "))
        list_item.append(num)
        print(list_item)
        calculate(list_item)

def calculate(list_item):
    sum_positive = 0
    sum_negative = 0

    for i in range(len(list_item)):
        if list_item[i] > 0:
            sum_positive = sum_positive + list_item[i]
        else:
            sum_negative = sum_negative + list_item[i]
    print(f'Sum of positive numbers = {sum_positive}')
    print(f'Sum of negative numbers = {sum_negative}')

if __name__ == "__main__":
    main()