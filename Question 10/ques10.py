print("\n2. Find biggest of 3 numbers entered.\n")
a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))

if a > b:
    if a > c:
        print(f'a={a} is greatest number')
    else:
        print(f'c={c} is greatest number')
else:
    if b > c:
        print(f'b={b} is greatest number')
    else:
        print(f'c={c} is greatest number')