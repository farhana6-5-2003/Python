#DATE : 08-10-2024
#2.Generate Fibonacci series of N terms

#PROGRAM

n=int(input("Enter the value for n :"))
f1=0
f2=1
print(f1)
print(f2)
for i in range(2,n):
	nt=f1+f2
	f1=f2
	f2=nt
	print(nt)
	
	

#OUTPUT

#Enter the value for n:5
#0
#1
#1
#2
#3

#Enter the value for n:10
#0
#1
#1
#2
#3
#5
#8
#13
#21
#34
