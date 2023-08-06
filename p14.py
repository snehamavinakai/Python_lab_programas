# 14. Write a python program to search an element using linear equation

list_item = []

def main():
    n = int(input("Enter number of values to be inserted :: "))

    for i in range(n):
        num = int(input("Enter the number :: "))
        list_item.append(num)
    print(list_item)
    
    key = int(input("Enter the element to be searched :: "))
    linearSearch(list_item, key)

def linearSearch(liat_item, key):
    found = False

    for i in range(len(list_item)):
        if liat_item[i] == key:
            found = True
            break
        
    if found == True:
        print(f'{key} is present at {i}th location.')
    else:
        print(f'{key} is not present')

if __name__ == "__main__":
    main()