class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side*self.side
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
def Show_area(self):
    print('Area is:',Shape.area())
s1=Square(4)
r1=Rectangle(5,10)
c1=Circle(4)
Show_area(s1)
Show_area(r1)
Show_area(c1)
#print(s1.area())
#print(r1.area())
#print(c1.area())
    
