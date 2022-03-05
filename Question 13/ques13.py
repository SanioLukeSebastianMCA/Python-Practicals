print("\n3. Accept an integer n and compute n+nn+nnn.\n")
sumval = 0
n = int(input("Enter the value for n : "))
for i in range(1, n + 1):
    sumval += n ** i
print(f'The result of the operation is : {sumval}')