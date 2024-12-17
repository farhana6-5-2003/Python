#Write a Python program to write a Python dictionary to a csv file. After writing the CSV file
#read the CSV file and display the content.
import csv
mydict=[{'branch':'COE','cgpa':'9.0','name':'Nikhil','year':'2'},
        {'branch':'IT','cgpa':'8.9','name':'Anu','year':'2'},
        {'branch':'SE','cgpa':'9.2','name':'Rahul','year':'3'},
        {'branch':'COE','cgpa':'9.5','name':'Miya','year':'2'},
        {'branch':'IT','cgpa':'8.8','name':'Tom','year':'1'},
        {'branch':'SE','cgpa':'8.6','name':'Jerry','year':'1'},
        {'branch':'EP','cgpa':'9.1','name':'Thomas','year':'3'}]
fields=['name','branch','year','cgpa']
filename="records.csv"
with open(filename,"w") as f:
	writer=csv.DictWriter(f,fieldnames=fields)
	writer.writeheader()
	writer.writerows(mydict)
f.close()

with open("records.csv","r") as f:
	row=csv.reader(f)
	for i in row:
		print(i)
f.close()
