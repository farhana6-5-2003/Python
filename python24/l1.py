
# DATE : 10-10-2024
#3.List comprehensions:

#a.Generate positive list of numbers from a given list of integers
#PROGRAM:

l=input("Enter the list of integers seperated by spaces:")
l1=[int(num) for num in l.split()]
pl=[num for num in l1 if num>0]
print("The list of positive numbers are:",pl)
p2=[num for num in l1 if num<0]
print("The list of negative numbers are:",p2)


#b.Square of N numbers
#PROGRAM:
s=input("Enter the list of integers seperated by spaces:")
s1=[int(num) for num in l.split()]
print(s1)




