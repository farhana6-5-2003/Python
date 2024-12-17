#Write a Python program to read a file line by line and store it into a list.
file=open("file1.txt","r")
l=[i.split() for i in open("file1.txt")]
print(l)
file.close()
