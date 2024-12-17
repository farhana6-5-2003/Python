#5.Create a class Publisher (name). Derive class Book from Publisher with attributes title and author. Derive class Python from Book with attributes price and no_of_pages. Write	a program that displays information about a Python book. Use base class constructor invocation and method overriding

class Publisher:
	def __init__(self,name):
		self.name=name
	def display():
		pass
		
	
class Book(Publisher):
	def __init__(self,name,title,author):
		super().__init__(name)   #invoking the base class constructor
		self.title=title
		self.author=author
	def display():
		pass
	
class Python(Book):
	def __init__(self,name,title,author,price,nopages):
		super().__init__(name,title,author)
		self.price=price
		self.nopages=nopages
	def display(self):
		print("\n-----------Book Details-----------")
		print("Title        : ",self.title)
		print("Name         : ",self.name)
		print("Author       : ",self.author)
		print("Price        : ",self.price)
		print("No. of Pages : ",self.nopages)

name=input("Enter Name :")
title=input("Enter Title:")
author=input("Enter Author:")
price=int(input("Enter Price:"))
nopages=int(input("Enter number of pages:"))

b=Python(name,title,author,price,nopages)
b.display()


