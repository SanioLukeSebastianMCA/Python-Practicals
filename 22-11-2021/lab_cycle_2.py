import math


def ques01():
    print("\n************************  1st Question  ************************\n\n")
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


def ques02():
    print("\n************************  2nd Question  ************************\n\n")
    print("Prompt the user for a list of integers. For all values greater than 100, store ‘over’ instead.")

    int_list = []
    size = int(input("Enter the size for the list : "))
    print("Enter the numbers in the list : ")
    for i in range(0, size):
        temp = int(input())
        if temp > 100:
            int_list.append("Over")
        else:
            int_list.append(temp)

    print(f'The created list is : {int_list}')


def ques03():
    print("\n************************  3rd Question  ************************\n\n")
    print("Store a list of first names. Count the occurrences of ‘a’ within the list")

    names = []
    count = 0
    size = int(input("Enter the size of the list of names : "))
    names = [str(input()) for i in range(size)]
    for i in names:
        for j in i:
            if j.lower() == 'a':
                count += 1

    print(f'Occurences of a in the list of first names is : {count}')


def ques04():
    print("\n************************  4th Question  ************************\n\n")

    list1 = [5, 6, 32, 6, 2]
    list2 = [39, 4, 6, 2]

    print(f'List 1 : {list1}')
    print(f'List 2 : {list2}')
    print("\n")
    print("(a) Whether list are of same length")
    if len(list1) == len(list2):
        print(f"The length of the both lists are same i.e. {len(list1)}")
    else:
        print(f"The lengths of two lists are different !! list1 -> {len(list1)} and list2 -> {len(list2)}")

    print("(b) whether list sums to same value")
    list1_sum = sum(list1)
    list2_sum = sum(list2)

    if list1_sum == list2_sum:
        print(f"The list sums are equal i.e. {list2_sum}")
    else:
        print(f"The list sums are diiferent : sum of list1 -> {list1_sum} and sum of list2 -> {list2_sum}")

    print("(c) whether any value occur in both")
    for i in list1:
        if i in list2:
            print(f"{i} occurs in both")


def ques05():
    print("\n************************  5th Question  ************************\n\n")
    print("Get a string from an input string where all occurrences of first character replaced with ‘$’,"
          " except first character. [eg: onion -> oni$n]")

    string = str(input("Enter the string word : "))
    first_char = string[0].lower()
    new_string = ""
    for i in range(len(string)):
        if i > 0 and string[i].lower() == first_char:
            new_string += '$'
        else:
            new_string += string[i]

    print(f'The string is : {string}')
    print(f'Newly formed string according to the question is : {new_string}')


def ques06():
    print("\n************************  6th Question  ************************\n\n")
    print("Accept the radius from user and find area of circle.")
    rad = int(input("Enter the radius : "))
    area = math.pi * (rad ** 2)
    print(f'Are of the circle with radius {rad} is {area} m2')


def ques07():
    print("\n************************  7th Question  ************************\n")
    print("Write a program to Print list in reverse order using a loop.")

    list = [4, 1.4, 53, 'Cain', 3]

    print(f'The list is : {list}')
    reversed_list = [list[i] for i in reversed(range(0, len(list)))]
    print(f'The list in reversed order is : {reversed_list}')
    print("\n")


def ques08():
    print("\n************************  8th Question  ************************\n")
    print("Create a single string separated with space from two strings by swapping the character at position 1.")

    string1 = str(input("Enter the string 1 : "))
    string2 = str(input("Enter the string 2 : "))

    temp = string1[0]
    string1 = string1.replace(string1[0], string2[0])
    string2 = string2.replace(string2[0], temp)
    result = string1 + " " + string2
    print(f'Result of the two strings : {result}')


def ques09():
    print("\n************************  9th Question  ************************\n\n")
    print("Write a Python Program for compound interest.")

    p = float(input("Enter the initial principal balance/amount : "))
    r = float(input("Enter the interest rate : "))
    t = int(input("Enter the time period : "))

    final_compound_interset = p * (1 + r / 100) ** t
    print(f'The compound interest of the amount according to the values entered : {final_compound_interset}')


def ques10():
    print("\n************************  10th Question  ************************\n\n")
    print("Implement Python Script to generate prime numbers series up to n.")
    n = int(input("Enter the limit for the series : "))

    print(f'The list of prime numbers until {n} are : ', end=' ')
    for i in range(2, n + 1):
        isPrime = 0
        for j in range(2, int(i / 2) + 1):
            if i % j == 0:
                isPrime = 1
                break

        if isPrime == 0:
            print(f'{i}, ', end=' ')


# 1. List comprehensions:
# (a) Generate positive list of numbers from a given list of integers
# (b) Square of N numbers
# (c) Form a list of vowels selected from a given word
# (d) List ordinal value of each element of a word (Hint: use ord() to get ordinal values)
ques01()

# 2. Prompt the user for a list of integers. For all values greater than 100, store ‘over’ instead.
ques02()

# 3. Store a list of first names. Count the occurrences of ‘a’ within the list
ques03()

# 4. Enter 2 lists of integers. Check
# (a) Whether list are of same length
# (b) whether list sums to same value
# (c) whether any value occur in both
ques04()

# 5. Get a string from an input string where all occurrences of first character replaced with ‘$’,
# except first character. [eg: onion -> oni$n]
ques05()

# 6. Accept the radius from user and find area of circle.
ques06()

# 7. Write a program to Print list in reverse order using a loop.
ques07()

# 8. Create a single string separated with space from two strings by swapping the character at
# position 1.
ques08()

# 9. Write a Python Program for compound interest.
ques09()

# 10. Implement Python Script to generate prime numbers series up to n.
ques10()
