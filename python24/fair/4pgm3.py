#3.Create a class Rectangle with private attributes length and width. Overload ‘<’ operator  to compare the area of 2 rectangles.

class Rectangle:
	def __init__(self,length,width):
		self.length=length
		self.width=width
		
	def area(self):
		return self.length*self.width
		
	def __lt__(self,other):
		return self.area() < other.area()

l1=int(input("Enter the length of Rectangle1:"))
w1=int(input("Enter the width of Rectangle1:"))
l2=int(input("Enter the length of Rectangle2:"))
w2=int(input("Enter the width of Rectangle1:"))

rect1=Rectangle(l1,w1)
rect2=Rectangle(l2,w2)
if rect1<rect2:
	print("Area of Rectangle1 is smaller than Area of Rectangle2")
elif(rect1>rect2):
	print("Area of Rectangle1 is larger than Area of Rectangle2")
else:
	print("Both Rectangles have same Area")
		
