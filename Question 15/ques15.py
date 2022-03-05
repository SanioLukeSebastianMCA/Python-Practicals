print("Create a single string separated with space from two strings by swapping the character at position 1.")

string1 = str(input("Enter the string 1 : "))
string2 = str(input("Enter the string 2 : "))

temp = string1[0]
string1 = string1.replace(string1[0], string2[0])
string2 = string2.replace(string2[0], temp)
result = string1 + " " + string2
print(f'Result of the two strings : {result}')