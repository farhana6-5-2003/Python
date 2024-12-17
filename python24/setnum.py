#DATE: 15-10-2024
#5.Prompt the user for a list of integers.For all values greater than 100,store 'Over' instead

uinput=input("Enter a List of Integers seperated by spaces:")
numbers=uinput.split()
result=[]
for x in numbers:
	num=int(x)
	if num>100:
		result.append('Over')
	else:
		result.append(num)
print("The List of Numbers:")
print(result)

#OUTPUT:
#Enter a List of Integers seperated by spaces:
#75 150 57
#The List of Numbers:
#['75','Over','57']

