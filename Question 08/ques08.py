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
