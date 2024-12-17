#DATE: 15-10-2024
#15.Print all colours from colour list1 not contained in colour list2.Create Colour List given a user input.Use List Comprehension
#PROGRAM:
list1=[i for i in input("Enter the colours in list1:").split()]
list2=[i for i in input("Enter the colours in list2:").split()]
result=[i for i in list1 if i not in list2]
print("Colours in List 1 not in List 2:")
print(result)
#OUTPUT:
#Enter the colours in list1:red blue green
#Enter the colours in list2:blue yellow white
#Colours in List 1 not in List 2:
#['red','green']

