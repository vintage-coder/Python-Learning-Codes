#This program finds the factorial of the given number
#This is the facrorial problem using the funtion
#This is factorial using recursion
def factorial(n):
	assert n>=0,"The factorial cannot be found for negative number"
	if n==0:
		return 1
	else:
		return n*factorial(n-1)



if __name__=="__main__":
	print("Enter the number to find out the factorial of the given number:",end='')
	n=int(input())
	print("The factorial is ",factorial(n))

#This is the new approach to solve the recurision using class 
#This is factorial using recursion
class factorial:
	def __init__(self,number):
		self.number=number

	def calculation(self):
		assert self.number>=0,"negative number not valid"

		if self.number==0:
			return 1
		else:
			temp=self.number
			self.number-=1
			return temp*self.calculation()


if __name__=='__main__':
	num=int(input("Enter the number to find factorial of the number:"))
	obj=factorial(num)

	print("The factorial of the given number is :",obj.calculation())



#This is factorial using normal function


def factorial(num):
	assert num>=0,"negative number not valid"
	fact=1
	if num==0:
		return 1
	else:
		
		for i in range(1,num+1):
			fact=fact*i
		return fact


if __name__=="__main__":
	n=int(input("Enter the number to calculate facrorial:"))
	print("The factorial is",factorial(n))



class factorial:
	def __init__(self):
		self.fact=1

	def calculation(self):
		num=int(input("Enter the number:"))
		assert num>=0,"negative number not valid"
		for i in range(1,num+1):
			self.fact=self.fact*i

		return self.fact

obj=factorial()
print("The factorial is ",obj.calculation())

















