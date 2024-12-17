#DATE : 29-10-2024
#20.From a list of integers, create a list removing even numbers
#From a list of integers, create a list removing even numbers.

#PROGRAM
ol=[int(i) for i in input("Enter the integers :").split()]
nl=[i for i in ol if i%2!=0]
print("List after removing even numbers :",nl)

#OUTPUT
#Enter the integers :12 34 55 5 7 23
#List after removing even numbers : [55, 5, 7, 23]

