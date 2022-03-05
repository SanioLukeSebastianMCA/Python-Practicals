print("\nAccept a file name from user and print extension of that.\n")
filename = input("Enter the full filename : ")
extension = filename.split(".")
print("Extension of the file is : " + extension[-1])
