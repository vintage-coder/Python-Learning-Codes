#The base class for all exception is "Exception"

#Exception hanling is very useful in any programming language it can handle any errors
#This will help the user to type the correct input value
#we can raise the excepion forcefully and that excetion can also be handled using the raise keyword
#That means we create a custom exception for a particular value


#Exception occurs block

try:
	n=int(input('Enter the number:'))
	if n<0:
		#The exception is cutomized by the programmer manually
		raise ValueError(n,"Input value should be greater than zero")
#Exception handling block
except ValueError as ve:
	#The raised exception is caught in the exception block
	print(ve)
#Execution block
finally:
	#This statement always executes even the exception occurs or not
	print('Executing remaining block..........')
	

#We can see what exeception has occured with out knowing what exception it is
#by the sys library
import sys

a=['name',23,1.4,0,True]

for items in a:
	try:
		print('The item is',items)
		entry=1/int(items)
		print('The reciprocal of ',items ,'is ',entry)
		print()
	except:
		print('oops the',sys.exc_info()[0],'occured')
		print()
	finally:
		print('Execution continues.........')
		print()

#Finally statement is very useful when closing the file if exception even occurs or not

try:
	file=open("gowtham.txt",'w+',encoding='utf-8')

except:
	print('file is not exists')

finally:
	file.close()



#Exceptions.................................

#Name Error 'x' is not defined

# for y in x:
# 	pass

#Syntax Error

# for in a:
# 	pass

#ZeroDivisionError

#1/0

#FileNotFoundError
#open("gowtham.txt")

#Type Error

#1/'gowtham'

#Import Error

#import gowtham (it is not a module)

#Assertion Error

# def function(a):
# 	assert a<=5 ,"The argument passed to the function greater than 5"
# 	#Assertion statement is like raise-if .that is it will raise if the condition
# 	#is false .it executes the statement is true.
# 	#It is very usefull when we debugging the programs
# 	print('Execution is sucessfull...')


# function(5)


#StopIteration

# a=(i for i in range(3))

# next(a)
# next(a)
# next(a)
# next(a) #The StopIteration exception is happening when the iteration not occurs

#KeyboardIntertupt

# import time

# for i in range(10):
# 	time.sleep(2)
# 	print(i)

# when we press ctrl+c the KeyboardIntertupt happens stoping the Execution


#Index Error

# a=[i for i in range(4)]

# a[5] #it causes the index error that is list out of range


#Key Error

# a={1:'gowtham',2:'hacker'}

# a[3] #It raises the key error because the key is not found in the dictionary

#Identation Error

# a={1:'gowtham',2:'hacker'}

# for i in a.values():
# print(i)  #it will raise the Identation Error


#We can also create our own exception using Exception baseclass inheriting
#The features

# class CalculationError(Exception):
# 	pass

# raise CalculationError("This is the example of CalculationError")