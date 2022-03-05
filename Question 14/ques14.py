color1 = ["Yellow", "Red", "Purple", "Violet", "Green", "Black", "Grey"]
color2 = ["Red", "Blue", "Green"]
print(f'Color list 1 : {color1}')
print(f'Color list 2 : {color2}')
print("\nTherefore, the colors that are not presented in Color List 1 from List 2 are : ", end=' ')
for i in color1:
    if color2.__contains__(i) == 0:
        print(f'{i}, ', end=' ')