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