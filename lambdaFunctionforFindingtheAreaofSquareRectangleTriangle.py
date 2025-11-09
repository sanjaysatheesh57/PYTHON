print("Program to find the area of a Square, Rectangle, and Right-angled Triangle")

square = lambda a: a*a
rect = lambda l,b: l*b
tri = lambda b,h: (b*h)//2

a = int(input("\nEnter the side of the square: "))
l = int(input("Enter the length of the rectangle: "))
b = int(input("Enter the breadth of the rectangle: "))
bh = int(input("Enter the base of the right-angled triangle: "))
h = int(input("Enter the height of the right-angled triangle: "))

print("\nAreas:")
print("Square =", square(a))
print("Rectangle =", rect(l,b))
print("Right-angled Triangle =", tri(bh,h))
