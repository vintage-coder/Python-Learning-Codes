#Generators are the simple form of iterators
#using generators we can make the iteration very smart
#It differs from iterators and normal functions

# if the function contain atleast one yield keyword then that function is called
#generator function
#Generator function will not execute the funtion entirely.it will save the state of execution
#The yield funtion returns the iterator object,and give the caller to return back

#normal function will return the entire result where as generator yield result on successive calls

import time

def generate(n):
	for i in n:
		time.sleep(0.5)
		yield i 
		print("The call back value is:",i)  #if the function contains the yield keyword then that funtion is known as generator function

	#Generators can hold the value of each successive calls

	yield "The first iterators over"

	for i in n:
		time.sleep(0.5)
		yield i #returns the iterator object 20 times

	yield "Second iterators over"


a=[i*i for i in range(4)]

for i in generate(a):#controls the evaluation of iterator and prints the result
	print(i)


w=(i for i in range(10)) #This is the short cutt to create the generator  function


#Generator are very more memory efficient when dealing with large amount of memory
#than iterators

#Fibonacci implementation

def fibo(limit):
		a,b=0,1
		n=0

		while n<limit:
			yield a#here callback occurs
			a,b=b,a+b
			n+=1

for i in fibo(5):
	print("The series",i)
