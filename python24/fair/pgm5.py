#DATE:15-10-2024
#Prompt the user for a list of integers for all values greater than 100 Store 'Over' instead.Use List Comprehension.
#PROGRAM
list=[i for i in input("Enter the list of integers separated by spaces:").split()]
result=[i for i in list if i>100]

