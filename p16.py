#16. Write a python program to insert a number in a sorted array

list_item = []

def main():
    n = int(input("Enter the number of values to be inserted :: "))

    for i in range(n):
        num = int(input("Enter a number :: "))
        list_item.append(num)
    print(list_item)
    num = int(input("Enter the element to be inserted in sorted list :: "))
    insert_num(num)

def insert_num(num):
    list_item.append(num)
    sort_list = sorted(list_item)
    print(sort_list)

if __name__ == "__main__":
    main()