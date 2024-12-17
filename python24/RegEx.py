import re
txt="A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.RegEx can be used to check if a string contains the       specified search pattern.1 2 3 4 50 78 A Z v b n"
x1=re.search("^A.*n$",txt)
if x1:
	print("match")
else:
	print("no match")
x2=re.findall("[arn]",txt)
if x2:
	print("match")
else:
	print("no match")
x3=re.sub("\s","78",txt)

if x3:
	print("match")
else:
	print("no match")
	
x4 = re.findall("ai", txt)
print(x4) 

x5 = re.search("\s", txt)
print("The first white-space character is located in position:", x5.start()) 
