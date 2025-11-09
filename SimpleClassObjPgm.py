class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def findArea(self):
        area = self.length * self.breadth
        print("Area of the rectangle:", area)
    def findPeremeter(self):
        peremeter = 2 * (self.length + self.breadth)
        print("Peremeter of the rectangle:", peremeter)


# --- main program ---
l = int(input("Enter the length of the rectangle: "))
b = int(input("Enter the breadth of the rectangle: "))

rect1 = Rectangle(l, b)   # object created, constructor called automatically
rect1.findArea()
rect1.findPeremeter()
