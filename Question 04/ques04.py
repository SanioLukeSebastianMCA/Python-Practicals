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
