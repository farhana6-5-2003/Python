#Get string of first and last 2 chars.

str1=input("Enter String:")
l=len(str1)
if l>3:
	first=str1[0:2]
	last=str1[-2:]
	print(first+last)
else:
	print("Not possible")
