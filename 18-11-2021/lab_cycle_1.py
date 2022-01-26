def ques01():
    print("\n1. Display future leap years from current year to a final year entered by user.\n")
    check = 1
    while check == 1:
        future_year = int(input("Enter any future year : "))

        if 2021 < future_year <= 9999:
            check = 0
            print(f"Following are the leap years till the year {future_year} : ")
            for i in range(2021, future_year):
                if i % 4 == 0:
                    print(i)
        else:
            print('Enter a valid year which is below year 9999 and higher than year 2021 !!')


def ques02():
    print("\n2. Find biggest of 3 numbers entered.\n")
    a = int(input("Enter the value of a : "))
    b = int(input("Enter the value of b : "))
    c = int(input("Enter the value of c : "))

    if a > b:
        if a > c:
            print(f'a={a} is greatest number')
        else:
            print(f'c={c} is greatest number')
    else:
        if b > c:
            print(f'b={b} is greatest number')
        else:
            print(f'c={c} is greatest number')


def ques03():
    print("\n3. Accept an integer n and compute n+nn+nnn.\n")
    sumval = 0
    n = int(input("Enter the value for n : "))
    for i in range(1, n + 1):
        sumval += n ** i
    print(f'The result of the operation is : {sumval}')


def ques04():
    print("\n4. Merge two dictionaries.\n")
    d1 = {"Name": "Daniel", "Age": 21}
    d2 = {"designation": "Data Analyst", "salary": 30000}
    print(f'Before : {d1}')
    d1.update(d2)
    print(f'After merging : {d1}')


def ques05():
    print("\n5. Find GCD (Greatest Common Divisor) or HCF (Highest Common Factor) of 2 numbers\n")

    num1 = int(input("Enter the number 1 : "))
    num2 = int(input("Enter the number 2 : "))
    keyval = num1 if num1 < num2 else num2
    hcf = 1

    for i in reversed(range(1, keyval)):
        if num1 % i == 0 and num2 % i == 0:
            hcf = i
            break

    print(f'The HCF or GCD of the numebers {num1} and {num2} is {hcf}')


def ques06():
    print("\n6. Print out all colors from color-list1 not contained in color-list2.\n")
    color1 = ["Yellow", "Red", "Purple", "Violet", "Green", "Black", "Grey"]
    color2 = ["Red", "Blue", "Green"]
    print(f'Color list 1 : {color1}')
    print(f'Color list 2 : {color2}')
    print("\nTherefore, the colors that are not presented in Color List 1 from List 2 are : ", end=' ')
    for i in color1:
        if color2.__contains__(i) == 0:
            print(f'{i}, ', end=' ')


def ques07():
    print("\n\n7. Sort dictionary in ascending and descending order.\n")
    d1 = {'Besanio': 31, 'Avil': 27, 'Tejas': 21, 'Nebin': 25, 'Vikram': 23, 'Winston': 12, 'Shantanu': 13, 'Vivek': 32,
          'Benjamin': 8, 'Valle': 32}

    print(f'Name list : {d1}\n')
    print(f'Ascending ordered name list : {dict(sorted(d1.items()))}')
    print(f'Decending ordered name list : {dict(sorted(d1.items(), reverse=True))}')


def ques08():
    print("\n8. From a list of integers, create a list removing even numbers.\n")
    int_list = []
    odd_list = []
    size = int(input("Enter how many numbers that you want to enter into the integer list : "))
    for i in range(0, size):
        num = int(input())
        int_list.append(num)

    print(f'The interger list created is : {int_list}')

    for i in int_list:
        if (i % 2) != 0:
            odd_list.append(i)

    print(f'The integer list that does not include even numbers is : {odd_list}')


def ques09():
    print("\n9. Count the occurrences of each word in a line of text.\n")
    text = str(input("Enter the text : "))
    split_words = text.lower().split()
    checked_list = []

    for i in range(len(split_words)):
        checked_list.append(split_words[i])
        count = 1
        if checked_list.count(split_words[i]) <= 1:
            for j in range(i + 1, len(split_words)):
                if split_words[i] == split_words[j]:
                    count += 1
            print(f'Occurences of "{split_words[i]}" is : {count}')


def ques10():
    print(
        "\n10. Create a string from given string where first and last characters exchanged. [eg: python - > nythop].\n")
    stringval = str(input("Enter a string : "))
    finalstrval = ""
    for i in range(len(stringval)):
        if i == 0:
            finalstrval += stringval[len(stringval) - 1]
        elif i == len(stringval) - 1:
            finalstrval += stringval[0]
        else:
            finalstrval += stringval[i]

    print(f'The final string after exchanging the first and the last characters is : {finalstrval}')


# 1. Display future leap years from current year to a final year entered by user.
#ques01()

# 2. Find biggest of 3 numbers entered.
#ques02()

# 3. Accept an integer n and compute n+nn+nnn.
ques03()

# 4. Merge two dictionaries.
# ques04()

# 5. Find GCD (Greatest Common Divisor) or HCF (Highest Common Factor) of 2 numbers
#ques05()

# 6. Print out all colors from color-list1 not contained in color-list2.
#ques06()

# 7. Sort dictionary in ascending and descending order.
# ques07()

# 8. From a list of integers, create a list removing even numbers.
#ques08()

# 9. Count the occurrences of each word in a line of text.
#ques09()

# 10. Create a string from given string where first and last characters exchanged. [eg: python - > nythop].
#ques10()
