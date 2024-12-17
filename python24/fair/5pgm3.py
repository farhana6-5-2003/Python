#Write a Python program to read specific columns of a given CSV file and print the content of the columns.

import csv
with open("student.csv",mode="r") as f:
	csvr=csv.reader(f)
	print(" CSV File ")
	for row in csvr:
		print(row)
f.close()
f=open("student.csv","r")
col=csv.reader(f)
print("Specific columns from CSV file")
print("------------------------------")
for i in col:
	print(i[1],i[3])
f.close()
