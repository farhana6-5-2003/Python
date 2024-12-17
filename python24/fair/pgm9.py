#DATE : 29-10-2024
#9.Create a string from given string where first and last characters exchanged.  

#PROGRAM
s=input("Enter a String:")
first=s[0]
last=s[-1]
newstring=last+s[1:-1]+first
print(newstring)

#OUTPUT
#Enter a String:python 
#nythop

