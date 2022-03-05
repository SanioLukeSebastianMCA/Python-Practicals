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