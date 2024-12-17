#Write a program to read  each row from the CSV file and print a list of strings
import csv
with open("student.csv",mode="r") as f:
	csvr=csv.reader(f)
	for row in csvr:
		print(row)
 
