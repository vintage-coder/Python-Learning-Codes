#iterator is an important function of object in python.we can make the object iterable using
#iterator protocols called __iter__,__next__ dunter methods

class Car:

	def __init__(self,color,price):
		self.color=color
		self.price=price

	#this dunder method is called when we invoke the iter() function
	#it must return the iterable object.
	def __iter__(self):
		self.count=0
		self.val=[i+4 for i in range(20)]
		return self
	#This dunder method evaluates object if iteration exceeds beyond the condition
	#it raises the stopiteration exception
	def __next__(self):

		if self.count<len(self.val):
			x=self.count
			self.count+=1
			return self.val[x]

		else:
			raise StopIteration   #This is the one type of exeception handling


#it only have the name ,price in the dictionary
obj=Car("Black",10000)#obj.__dict__ only prints the initial initialisation of Car class
print(obj.__dict__)

for i in obj: #The object now is iterable.It prints all the count value
	print(i) #for loop operation creates the iterator of obj using iter() then evalutes the
	#value in the obj by next() using try except keyword 

#For loop can handle the iteration error where as the next() cannot handle stopiteratio exception.

#once the onject iteated .now, obj.__dict__ contains the val,count,price,and color instance 
#attributes
print(obj.__dict__)


#Finally iterator is so complex to write the iteration.To boost this operation
#Generators are mostly used.


#For loop will look like this:

# myiter=iter(obj)
# try:
# 	value=next(myiter)

# except StopIteration:
# 	break