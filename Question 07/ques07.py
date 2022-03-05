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
