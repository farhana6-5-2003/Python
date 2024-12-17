#Replace first char occurrences with $.
str1=input("Enter string:")
first=str1[0]
newstr=str1.replace(first,'$')
print(first+newstr[1:])
