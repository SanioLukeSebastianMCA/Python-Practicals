class rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

    def peri(self):
        print("Perimeter of the rectangle is : ", (2 * (self.l + self.b)))

    def compare(self, obj):
        if self.area() == obj.area():
            print("Both rectangles are equal.")
        else:
            print("Both rectangles are not equal.")


rec1 = rectangle(5, 2)
rec1_a = rec1.area()
print("Area of rectangle 01 : ", rec1_a)
rec1.peri()
rec2 = rectangle(4, 10)
rec2_a = rec2.area()
print("Area of rectangle 02 : ", rec2_a)
rec2.peri()
rec1.compare(rec2)
