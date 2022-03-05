print("\nCreate a list of colors from comma-separated color names entered by user. Display first and last colors.\n")
size = int(input("Enter the size of the color list : "))
print("Enter the color list items : ", end="")
colorlist = [str(x) for x in input("Enter the color list items : ").split(', ')]
print(f"The first color from the list is : {colorlist[0]}")
print(f"The last color from the list is : {colorlist[len(colorlist) - 1]}")
