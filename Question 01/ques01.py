print("\n1. Display future leap years from current year to a final year entered by user.\n")
check = 1
while check == 1:
    future_year = int(input("Enter any future year : "))

    if 2021 < future_year <= 9999:
        check = 0
        print(f"Following are the leap years till the year {future_year} : ")
        for i in range(2021, future_year):
            if i % 4 == 0:
                print(i)
    else:
        print('Enter a valid year which is below year 9999 and higher than year 2021 !!')
