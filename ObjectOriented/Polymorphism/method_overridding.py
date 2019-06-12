#Method overridding means that over writting the method  in the child class from parrent class
#The method name is same 


class Dove:
	def __init__(self,age=10):
		self.age=age

	def ageing(self):
		print('The age of bird is:',self.age)
	def singing(self):
		print("Dove won't sing no more")

class Kukoo(Dove):
	def __init__(self):
		self.singing()
		super().__init__()
		#This is the only way of calling parrent class overridden method
		super().singing()
	#The singing method is overridden from the base class
	def singing(self):
		print('Kukkoo is singing')
	#This is is also overridden method
	def ageing(self):
		print('The age of bird is',self.age+5)


obj=Kukoo()
#This method calling is not call the parrent class singing method
#This only work in child class
obj.singing()
#Calling the ageing method
obj.ageing()

dove=Dove()
#now clears that using the parrent class instance we can invoke the singing method or parrent method
#That is to be overridden by child class method

dove.singing()

#Another way ,we can call the parrent class method by super() function it creates 
#the proxy object of parrent class thus,we can call inside the childclass of parrent class
# singing method
