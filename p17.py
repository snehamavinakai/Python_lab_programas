#17. Write a program to stimulate stack operation

stack = []
stack_size = 5

def main():
    while True:
        print("Enter your choice :: ")
        ch = int(input("1.Push\n2.Pop\n3.Display\n"))

        if ch == 1:
            num = int(input("Enter number to be inserted :: "))
            push_item(num)
        elif ch == 2:
            pop_item()
        elif ch == 3:
            display()
        else:
            print("Invalid choice")
            val = input("Do you want continue(yes/no)")
            if val == 'no':
                break

def push_item(item):
    if(len(stack) < stack_size):
        stack.append(item)
    else:
        print("Stack is full")

def pop_item():
    if(len(stack) > 0):
        print(f'Item Deleted = {stack.pop()}')
    else:
        print('Stack is Empty')

def display():
    print("Elements of stack are :")
    for i in stack:
        print(i)
    print("Stack is Empty")

if __name__ == "__main__":
    main()