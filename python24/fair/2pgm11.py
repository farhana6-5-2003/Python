#DATE : 29-10-2024
#11.Write lambda functions to find area of square, rectangle and triangle.

#PROGRAM
area1=lambda a: a*a
area2=lambda l,b : l*b
area3=lambda b,h : 0.5*b*h
s=int(input("Enter the side of the square:"))
print("Area of the Square is ",area1(s))
leng=int(input("Enter the length of rectangle:"))
bred=int(input("Enter the breadth of rectangle:"))
print("Area of Rectangle is ",area2(leng,bred))
b1=int(input("Enter the base of triangle:"))
h1=int(input("Enter the height of triangle:"))
print("Area of Triangle is ",area3(b1,h1))

#OUTPUT
#Enter the side of the square:5
#Area of the Square is  25
#Enter the length of rectangle:12
#Enter the breadth of rectangle:6
#Area of Rectangle is  72
#Enter the base of triangle:5
#Enter the height of triangle:15
#Area of Triangle is  37.5

