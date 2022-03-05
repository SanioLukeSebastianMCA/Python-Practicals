from graphics import circle

r = int(input("Enter the radius of the circle : "))
circle.cir(r)

from graphics import rectangle

length = int(input("Enter the length of the rectangle : "))
breadth = int(input("Enter the breadth of the rectangle : "))
rectangle.rectt(length, breadth)

from graphics.package import cuboid

l = int(input("Enter the length of the cuboid : "))
w = int(input("Enter the width of the cuboid : "))
h = int(input("Enter the height of the cuboid : "))
b = int(input("Enter the breadth of the cuboid : "))
cuboid.cubo(l, w, h, b)

from graphics.package import sphere

r = int(input("Enter the radius of sphere : "))
sphere.sphe(r)
