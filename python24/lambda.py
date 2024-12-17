#Write Lambda functions to finf the sum of 3 numbers,product of 3 numbers

sum=lambda a,b,c:a+b+c
product=lambda a,b,c:a*b*c
a=int(input("Enter num1:"))
b=int(input("Enter num2:"))
c=int(input("Enter num3:"))
print("Sum of the 3 numbers is",sum(a,b,c))
print("Product of the 3 numbers is",product(a,b,c))
