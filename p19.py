#19. Write a python program programs to using the built-in methods of the string, list and dictionary classes

#String built-in methods
string = "Hello, World!"
length = len(string)
print("Length of string is : ",length)

upper_case = string.upper()
print("Uppercase String : ",upper_case)

lower_case = string.lower()
print("Lowercase String : ",lower_case)

count = string.count("o")
print("Number of 'o' in the string", count)


#List built-in methods
my_list = [1,2,3,4,5]
length = len(my_list)
print("\nLength of list :", length)

my_list.append(6)
print("List after appending element :", my_list)

my_list.sort()
print("Sorted list :",my_list)

my_list.reverse()
print("Reversed list : ",my_list)

#Dictinory built-in methods
my_dict = {"name":"John","age":25,"city":"New York"}
length = len(my_dict)
print("\nLength of dictionary :", length)

key = my_dict.keys()
print("Key in dictionary :",key)

values = my_dict.values()
print("Values in dictionary are : ", values)

key_exists = "age" in my_dict
print("Does 'age exists in dictinory ?",key_exists)

my_dict.pop("age")
print("Dictionary after removing age", my_dict)