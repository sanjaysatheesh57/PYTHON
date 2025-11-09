class Student:
    "Common base class for all students"
    def getData(self,rollno,name,course):
        self.rollno = rollno
        self.name = name
        self.course = course

    def displayStudent(self):
        print("Roll number:", self.rollno)
        print("Name:", self.name)
        print("Course:", self.course)
    #Inheritance
class Test(Student):
    def getMarks(self, marks):
        self.marks = marks

    def displayMarks(self):
        print("Total Marks:", self.marks)

r = int(input("Enter the Roll Number: "))
n = input("Enter Name: ")
c = input("Enter Course Name: ")
m = int(input("Enter Marks: "))
    #Creating object

print("Result")
stud1 = Test()
stud1.getData(r ,n ,c)
stud1.getMarks(m)
stud1.displayStudent()
stud1.displayMarks()



