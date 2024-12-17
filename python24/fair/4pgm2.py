#2.Create a Bank account with members account number, name, type of account and balance. Write constructor and methods to deposit at the bank and withdraw an amount from the bank.

class Account:
	def __init__(self,accno,aname,acctype,balance):
		self.accno=accno
		self.aname=aname
		self.acctype=acctype
		self.balance=balance
			
	def deposit(self,amt):
		if amt>0:
			self.balance+=amt
			print("Successfully Deposited ",amt)
		else:
			print("Invalid Amount")
		
	def withdraw(self,amt):
		if amt>self.balance:
			print("Insufficient Balance")
		else:
			self.balance-=amt
			print("Successfully withdrawn ",amt)
		
	def viewDetails(self):
		print("\nAccount Number  : ",self.accno)
		print("Account Name    : ",self.aname)
		print("Account Type    : ",self.acctype)
		print("Account Balance : Rs.",self.balance,"\n")
                
                

accno=int(input("Enter account number :"))
aname=input("Enter account name :")
acctype=input("Enter account type:")
balance=int(input("Enter account balance :"))

c1=Account(accno,aname,acctype,balance)

while True:
	print("----------MENU------------\n1. Deposit\n2. Withdraw\n3. Currect Balance\n4. View Details\n5. Exit")
	ch=int(input("Enter your choice :"))
	if ch==1:
		amt=int(input("Enter the amount to be deposited:"))
		c1.deposit(amt)
	elif ch==2:
		amt=int(input("Enter the amount to be withdrawn:"))
		c1.withdraw(amt)
	elif ch==3:
		print("\nCurrent Balance : Rs.",c1.balance,"\n")
		
	elif ch==4:
		c1.viewDetails()
	elif ch==5:
	        break
	

                
		
