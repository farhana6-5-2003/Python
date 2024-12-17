#display future leap years from current year to final year from user

final=int(input("Enter the final year:"))
year=2024
year=year+1
while(year<=final):
	if (year%4==0 and year%100!=0 or year%400==0):
		print(year,"  ")
	year=year+1
	
	
