print("Store a list of first names. Count the occurrences of ‘a’ within the list")
count = 0
size = int(input("Enter the size of the list of names : "))
names = [str(input()) for i in range(size)]
for i in names:
    for j in i:
        if j.lower() == 'a':
            count += 1

print(f'Occurences of a in the list of first names is : {count}')
