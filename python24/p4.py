#write a program to input 2 integers and print largest among two.

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
if a>b:
  print(a,"is greater than ",b)
elif b>a:
  print(b,"is greater than ",a)
else:
  print(a,"equal to ",b)
