print("Program to find the factorial of a number.")

num = int(input("Enter the factorial Number : "))
fact = 1
for i in range(0, num):
    fact += fact * i

print(f'The factorial number the number ({num}) is : {fact}')
print("\n")