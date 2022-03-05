num1 = int(input("Enter the number 1 : "))
num2 = int(input("Enter the number 2 : "))
keyval = num1 if num1 < num2 else num2
hcf = 1

for i in reversed(range(1, keyval)):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
        break

print(f'The HCF or GCD of the numebers {num1} and {num2} is {hcf}')