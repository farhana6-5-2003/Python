#Create a dictionary of 5 countries and their capitals.Write a function to take a country as input and return its capital


def c_capital(dict1,cname):
	if cname in dict1:
		print("Capital is :",dict1[cname])
	else:
		print(".....Not in Dictionary.....")


dict1={"India":"Delhi",
	"America":"Washington",
	"South Korea":"Seoul",
	"Japan":"Tokyo",
	"Saudi Arabia":"Riyadh"}
cname=input("Enter Country name:")
c_capital(dict1,cname)

	
