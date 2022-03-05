print("(a) Generate positive list of numbers from a given list of integers")

integers = [-10, 1, 23, 5, -1.2, 5, 10, 54, 100.1, 42]
positive_integers = [pos_num for pos_num in integers if pos_num > 0]
print(f"List of positive integers is : {positive_integers}")

print("\n(b) Square of N numbers")
n = int(input("Enter the value of N : "))
print(f"Squares of 1 to {n} are : ")
sqr_num_list = [num ** 2 for num in range(1, n + 1)]
for i in range(0, len(sqr_num_list)):
    print(f"{i} -> {sqr_num_list[i]}")

print("\n(c) Form a list of vowels selected from a given word")
vowels = ['a', 'e', 'i', 'o', 'u']
word = str(input("Enter the string : "))
print("The vowels in the word given are : ")

vowel_list = [chr for chr in word.lower() if chr in vowels]
for i in vowel_list:
    print(f'{i}, ', end=" ")
print("")

print("\n(d) List ordinal value of each element of a word (Hint: use ord() to get ordinal values)")
word = str(input('Enter the word : '))
ord_list = [ord(ch) for ch in word]
for i in range(0, len(ord_list)):
    print(f"{word[i]} -> {ord_list[i]}")
print()
