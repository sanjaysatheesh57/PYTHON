


#This is a program to demonstrate the use of split function in list. for example, taking a file name as input and printing its file extension as output.

filename= input("Enter the file name")
parts= filename.split(".")
print("The extension is: ", parts[-1])
