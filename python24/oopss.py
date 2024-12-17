#1.Create a class student with attributes number,name and age. Create an object student1 of the student class.Print the rollno,name and age,
class Student:
	def __init__(self,no,name,age):
		self.no=no
		self.name=name
		self.age=age
student1=Student('101','Neenu','15')
print("RollNo : ",student1.no)
print("Name   : ",student1.name)
print("Age    : ",student1.age)
	
