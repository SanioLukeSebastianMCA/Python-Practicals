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