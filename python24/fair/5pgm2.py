#Python program to copy odd lines of one file to other

f=open("file1.txt","r")
g=open("file2.txt","w")
print("In File1:")
lno=1
for line in f:

   if lno%2!=0:
       g.write(line)
   lno=lno+1
       
g.close()
g=open("file2.txt","r")      
print(g.read())
g.close()
f.close()
f=open("file1.txt","r")
g=open("file3.txt","w")
print("In File2:")
ln=1
for line in f:
	if ln%2==0:
	   g.write(line)
	ln=ln+1
g.close()
g=open("file3.txt","r")
print(g.read())
g.close()
