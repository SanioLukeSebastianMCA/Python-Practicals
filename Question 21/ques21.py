print("Generate Fibonacci series of N terms.")

first = 0
second = 1
n = int(input("Enter the N term for Fibonacci series (Please enter a number greater than 2 !!) : "))
print(f'The fibonaaci series of N={n} numbers is : ', end=' ')
for i in range(0, n):
    if i > 1:
        temp = first
        first = second
        second = temp + first
        print(f'{second}, ', end=' ')
    else:
        print(f'{i}, ', end=' ')
print("\n")