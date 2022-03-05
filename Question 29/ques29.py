print("Generate all factors of a number.")

num = int(input("Enter the number to find the factor : "))
print(f"The factors of the given number ({num}) are : ", end=' ')
for i in range(1, num + 1):
    if num % i == 0:
        print(f'{i}, ', end=' ')
print("\n")