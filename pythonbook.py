class Publisher:
    def getdata(self,name):
        self.name=name
    def displaypublisher(self):
        print("Publisher Name:",self.name)
class Book(Publisher):
    def getinfo(self,title,author):
        self.title=title
        self.author=author
    def displayinfo(self):
        print("Title Name:",self.title)
        print("Author Name:",self.author)
class Python(Book):
    def getdetails(self,price,pageno):
        self.price=price
        self.pageno=pageno
    def displaydetails(self):
        print("Price:",self.price)
        print("pageno:",self.pageno)
p=str(input("Enter The Publisher Name:"))
t=str(input("Enter The Title:"))
a=str(input("Enter The Author Name:"))
pr=int(input("Enter The price:"))
page=int(input("Enter The No Of Pages:"))
obj=Python()
obj.getdata(p)
obj.getinfo(t, a)
obj.getdetails(pr, page)
print("\n----- Book Details -----")
obj.displaypublisher()
obj.displayinfo()
obj.displaydetails()





