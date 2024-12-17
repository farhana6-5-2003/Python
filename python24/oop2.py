class Student:
	def __init__(self,no,name,age):
		self.no=no
		self.name=name
		self.age=age
rollno=int(input("Enter rollno:"))
name=input("Enter name:")
age=int(input("Enter age:"))
student1=Student(rollno,name,age)
print()
print("RollNo : ",student1.no)
print("Name   : ",student1.name)
print("Age    : ",student1.age)
