def ques01():
    print("\n************************  1st Question  ************************\n")
    print("Program to find the factorial of a number.")

    num = int(input("Enter the factorial Number : "))
    fact = 1
    for i in range(0, num):
        fact += fact * i

    print(f'The factorial number the number ({num}) is : {fact}')
    print("\n")


def ques02():
    print("\n************************  2nd Question  ************************\n")
    print("Generate Fibonacci series of N terms.")

    first = 0
    second = 1
    n = int(input("Enter the N term for Fibonacci series (Please enter a number greater than 2 !!) : "))
    print(f'The fibonaaci series of N={n} numbers is : ', end=' ')
    for i in range(0, n):
        if i > 1:
            temp = first
            first = second
            second = temp + first
            print(f'{second}, ', end=' ')
        else:
            print(f'{i}, ', end=' ')
    print("\n")


def ques03():
    print("\n************************  3rd Question  ************************\n")
    print("Find the sum of all items in a list.")

    list = [21, 25, 53, 1, 156, 9, 87, 10]
    sum = 0
    print(f'The list is : {list}')
    sum += [1 for i in list]
    print(f'The sum of all items in the list is : {sum}')
    print("\n")


def ques04():
    print("\n************************  4th Question  ************************\n")
    print("Write lambda functions to find area of square, rectangle and triangle.")

    print("Area of Square")
    l = float(input("Enter the length of a side of a square : "))
    area_sqr = lambda a: a ** 2
    print(f'Area of a square with side length={l} is {area_sqr(l)} sqm')
    print("\n")

    print("Area of Rectangle")
    length = float(input("Enter the length : "))
    breadth = float(input("Enter the breadth : "))
    area_rec = lambda a, b: a * b
    print(f'Area of a rectangle with side length={length} & breadth={breadth} is {area_rec(length, breadth)} sqm')
    print("\n")

    print("Area of triangle.")
    length = float(input("Enter the length : "))
    breadth = float(input("Enter the breadth : "))
    area_tri = lambda a, b: 0.5 * a * b
    print(f'Area of a triangle with side length={length} & breadth={breadth} is {area_tri(length, breadth)} sqm')
    print("\n")


def ques05():
    print("\n************************  5th Question  ************************\n")
    print("Generate all factors of a number.")

    num = int(input("Enter the number to find the factor : "))
    print(f"The factors of the given number ({num}) are : ", end=' ')
    for i in range(1, num + 1):
        if num % i == 0:
            print(f'{i}, ', end=' ')
    print("\n")


def ques06():
    # num_list = []
    # print(f"Enter the {size} even valued 4-digit numbers : \n")
    # for i in range(0, size):
    #     all_even = False
    #     while not all_even:
    #         num = int(input())
    #         check_num = True
    #         for j in str(num):
    #             if int(j) % 2 != 0:
    #                 check_num = False
    #                 break
    #         all_even = check_num
    #         if not check_num:
    #             print("Digits not even. Please enter a numbers with all even digits !!")
    # print(list)

    print("\n************************  6th Question  ************************\n")
    print("Generate a list of four digit numbers in a given range with all their digits even and the number is a "
          "perfect square.")
    l_limit = int(input("Enter the lower limit : "))
    h_limit = int(input("Enter the higher limit : "))
    print("The numbers which are perfect square within the given limits are : ")
    for i in range(l_limit, h_limit + 1):
        if i ** 0.5 == int(i ** 0.5):
            print(f'{i}, ', end=' ')
    print("\n")


def ques07():
    print("\n************************  7th Question  ************************\n")
    print("Accept a list of words and return length of longest word.")
    size = int(input("Enter the size for the word list : "))
    print("Enter the list of words : ")
    list = []
    len_list = []
    for i in range(0, size):
        val = str(input())
        list.append(val)
        len_list.append(len(val))

    print(f'The length of the longest word in the list is : {max(len_list)}')
    print("\n")


def ques08():
    print("\n************************  8th Question  ************************\n")
    print("Count the number of characters (character frequency) in a string.")
    text = str(input("Enter the string : "))
    split_words = list(text.lower())
    checked_list = []

    for i in range(len(split_words)):
        checked_list.append(split_words[i])
        count = 1
        if checked_list.count(split_words[i]) <= 1:
            for j in range(i + 1, len(split_words)):
                if split_words[i] == split_words[j]:
                    count += 1
            print(f'Character frequency of "{split_words[i]}" is : {count}')
    print("\n")


def ques09():
    print("\n************************  9th Question  ************************\n")
    print("Add ‘ing’ at the end of a given string. If it already ends with ‘ing’, then add ‘ly’")
    string = str(input("Enter the string : "))
    third_last_strlen = len(string) - 3
    last_str = ''
    for i in range(0, 3):
        last_str = last_str + string[third_last_strlen + i]

    if last_str == 'ing':
        string = string + 'ly'
    else:
        string = string + 'ing'

    print(f'The modified string accordingly is : {string}')
    print("\n")


def ques10():
    print("\n************************  10th Question  ************************\n")
    print("Display the given pyramid with step number accepted from user.")

    limit = int(input("Enter the limit : "))
    for i in range(1, limit + 1):
        for j in range(1, i + 1):
            print(i * j, end=' ')
        print()
    print("\n")


def ques11():
    print("\n************************  11th Question  ************************\n")
    print("Construct following pattern using nested loop.")
    print("The constructed pattern is : ")
    count = 1
    for i in range(1, 8):

        if i <= 4:
            count = count + 1
        else:
            count = count - 1

        for j in range(1, count):
            print('*', end=' ')
        print()
    print("\n")


# 1. Program to find the factorial of a number.
# ques01()

# 2. Generate Fibonacci series of N terms.
# ques02()

# 3. Find the sum of all items in a list.
# ques03()

# 4. Write lambda functions to find area of square, rectangle and triangle.
# ques04()

# 5. Generate all factors of a number.
# ques05()

# 6. Generate a list of four-digit numbers in a given range with all their digits even and the number is a perfect
# square.
# ques06()

# 7. Accept a list of words and return length of the longest word.
# ques07()

# 8. Count the number of characters (character frequency) in a string.
# ques08()

# 9. Add ‘ing’ at the end of a given string. If it already ends with ‘ing’, then add ‘ly’.
ques09()

# 10. Display the given pyramid with step number accepted from user.
# ques10()

# 11. Construct following pattern using nested loop.
# ques11()
