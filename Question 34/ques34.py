class Rectangle:
    def __init__(self, l, b):
        self._l = l
        self._b = b

    def area(self):
        area1 = self._l * self._b
        return area1

    def __lt__(self, obj):
        if (self.area() < obj.area()):
            return "The area of rectangle A is less than Rectangle B"
        else:
            return "The area of rectangle B is less than Rectangle A"


print("Rectangle A\n")
l1 = int(input("Length of Rectangle A : "))
b1 = int(input("Breadth of Rectangle A : "))
obj1 = Rectangle(l1, b1)
print("The Area of Rectangle A is : ", obj1.area())

print("\nRectangle B")
l2 = int(input("Length of Rectangle B : "))
b2 = int(input("Breadth of Rectangle B : "))
obj2 = Rectangle(l2, b2)
print("The area of Rectangle 2 is : ", obj2.area())
print(f"\nAfter comparing, {obj1 < obj2}")
