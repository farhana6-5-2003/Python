#1.Create Rectangle class with attributes length and breadth and methods to find area and perimeter. Compare two Rectangle objects by their area

class Rectangle:
	def __init__(self,length,breadth):
		self.length=length
		self.breadth=breadth
	def area(self):
		return self.length*self.breadth
	def perimeter(self):
		return 2*(self.length+self.breadth)
len1=int(input("Enter length of rectangle1:"))
bread1=int(input("Enter breadth of rectangle 1:"))
len2=int(input("Enter length of rectangle1:"))
bread2=int(input("Enter breadth of rectangle 1:"))
rect1=Rectangle(len1,bread1)
rect2=Rectangle(len2,bread2)

if rect1.area()>rect2.area():
	print("Area of Rectangle1 is greater than Rectangle2")
elif rect1.area()<rect2.area():
	print("Area of Rectangle2 is greater than Rectangle1")
else:
	print("Area of two rectangles is Equal")




'''	
Enter length of rectangle1:20
Enter breadth of rectangle 1:10
Enter length of rectangle1:15
Enter breadth of rectangle 1:4
Area of Rectangle1 is greater than Rectangle2

Enter length of rectangle1:12
Enter breadth of rectangle 1:5
Enter length of rectangle1:13
Enter breadth of rectangle 1:6
Area of Rectangle2 is greater than Rectangle1
'''

