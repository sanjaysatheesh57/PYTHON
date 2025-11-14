class Student:
    def getdata(self,rollno,name,course):
        self.rollno=rollno
        self.name=name
        self.course=course
    def displayStudent(self):
        print("Rollno:",self.rollno)
        print("Name:",self.name)
        print("Course:",self.course)
class Test(Student):
    def getMarks(self,marks):
        self.marks=marks
    def displayMarks(self):
        print("Total Marks:",self.marks)
class Sports:
    def getSportsMarks(self,spmarks):
        self.spmarks=spmarks
    def displaySportsMarks(self):
        print("Sports Marks:",self.spmarks)
class Result(Test,Sports):
    def calculateGrade(self):
        m=self.marks+self.spmarks
        if m>480:
            self.grade="Distinction"
        elif m>360:
            self.grade="First Class"
        elif m>240:
            self.grade="Second Class"
        else:
            self.grade="Failed"
        print("Result:",self.grade)
r=int(input("Enter Roll Number:"))
n=input("Enter Name:")
c=input("Enter Course Name:")
m=int(input("Enter Marks:"))
s=int(input("Enter Sports marks:"))
print("Result")
stud1=Result()
stud1.getdata(r,n,c)
stud1.getMarks(m)
stud1.getSportsMarks(s) 
stud1.displayStudent() 
stud1.displayMarks() 
stud1.displaySportsMarks() 
stud1.calculateGrade() 
