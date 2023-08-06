#12. Write a python program to read aa word and print the number of letters ,vowels in the word

val = input("Enter a the string :: ")
count = 0
val = val.lower()

for i in val:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count += 1
if count == 0:
    print(f"The entered string {val} has no vowels")

else:
    print("Total vowels are :: ", count)

print(f'Total number of letters :: {len(val)}')