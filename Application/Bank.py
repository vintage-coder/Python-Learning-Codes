import random
import time
from getpass import getpass
import sys
class BankAccount:
	
	count=0
	def __init__(self,name=None,account_number=None):
		self.name=name
		self.account_number=account_number
		self.count+=1
		self.user={}
		self.values={}

	def run(self):
		print("Banking status on")
		while True:
			self.menu()
			choice=int(input("Enter your choice:"))
			if choice==1:
				self.create_account()
			elif choice==2:
				self.deposit_money()
			elif choice==3:
				self.withdraw_money()
			elif choice==4:
				self.display_amount()
			elif choice==5:
				self.exit()
			else:
				print("invlid choice")

				
			



	def create_account(self):
		print("Account Activation Details")
		detail=[]
		name=input("Enter your name:")
		account=input("Enter the account type:")
		detail.append(name)
		detail.append(account)
		print("your initial amount is 0")
		detail.append(0)
		account_number=random.randint(10000,99999)
		print("Account is being created. please wait............")
		time.sleep(5)
		self.user[account_number]=detail
		print("Account was created.Thank you")



		

	def deposit_money(self):
		print("Enter your account Number:",end='')
		no=int(input())
		if self.user.get(no,None):
			amount=int(input("Enter the amount to deposit:"))
			self.user[no][2]+=amount
			print("The amount {} successfully deposited".format(amount))
		else:
			print("Invalid Account")

		

	def withdraw_money(self):
		print("Enter the account Number to withdrawl money:",end='')
		no=int(input())
		if self.user.get(no,None):
			amount=int(input("Enter the amount to debit:"))
			self.user[no][2]-=amount
			print("The amount {} successfully debited".format(amount))
		else:
			print("Invalid account.Please Try again Later")

	def menu(self):
		print("1.Create Account")
		print("2.Deposit Money")
		print("3.WithDraw Money")
		print("4.Display Balance")
		print("5.Exit")
		

	def display_amount(self):
		print("Login Details")
		print("1.Admin")
		print("2.User")
		choice=int(input("Enter your choice:"))
		if choice==1:
			user_name=input("-------------->Enter your username:")
			password=getpass("-------------->Enter your password")
			if user_name=="gowthaman" and password=='12345':
				print("You successfully logged into the account")
				print("Do you want to see the account holder details(Y/N)?",end ='')
				val=input()
				if val=='y' or val=='Y':
					for i, j in self.user.items():
						print("AccountNumber=",i,"name and type",j)
				else:
					print("You are selected No")
			else:
				print("password is incorrect.please try again later.")
		elif choice==2:
			user_name=input("--------------->Enter your username:")
			password=getpass("---------------Enter your password:")
			if user_name=="gowthaman" and password=='54321':
				print("You successfully logged into the user account")
			else:
				print("Invalid password or username.Try again later.")
		else:
			print("Invalid choice.Choose the correct choice.Thank you!")

			
	def exit(self):
		a=input("press any key to exit................")
		sys.exit()



if __name__=="__main__":
	
	obj=BankAccount()
	obj.run()
