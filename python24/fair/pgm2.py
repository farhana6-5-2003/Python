#CO-1
#DATE : 08-10-2024
#2.Display future leap years from current year to a final year entered by user.

#PROGRAM

final=int(input("Enter the final year:"))
year=2024
year=year+1
print("The future leap years upto ",final," are :")
while(year<=final):
	if (year%4==0 and year%100!=0 or year%400==0):
		print(year,"  ")
	year=year+1

 
#OUTPUT:
#Enter the final year: 2050
#The future leap years upto 2050 are :
#2028
#2032
#2036
#2040
#2044
#2048


#Enter the final year: 2038
#The future leap years upto 2050 are :
#2028
#2032
#2036




