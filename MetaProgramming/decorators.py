#Time calculation of function to be executed
#Decorator is a function it takes the function as a argument and extends some behaviour
#of latter function is called decorator


#Programmers can add extra funtionality to add a wrapper around the funtion to add extra
#funtionality as timing and logging etc.

import time
from functools import wraps


#Decorator function
def timer(func):
	#This is wrapper function
	def wrapper(*args,**kwargs):
		start=time.time()
		print('The arguments are:',args,kwargs)
		result=func(*args,**kwargs)
		print('The result is :',result)
		end=time.time()
		print('Time elapsed:',(end-start)*1000)
		
		return result

	return wrapper



@timer
def time_calculation(n):
	
	sumof=0
	while 0<=n:
		sumof+=n
		n-=1
	return sumof











