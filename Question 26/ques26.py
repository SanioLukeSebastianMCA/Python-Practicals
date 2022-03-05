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