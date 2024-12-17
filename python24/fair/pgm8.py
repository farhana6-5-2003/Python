#DATE: 24-10-24
#Get a string from an input string where all occurrences of first character replaced with ‘$’, except first character

#PROGRAM
s=input("Enter string:")
c=s[0]
str1=s[1:]
if c in str1:
	new=str1.replace(c,"$")
print(c+new)

#OUTPUT
#Enter string:hehihi
#he$i$i

