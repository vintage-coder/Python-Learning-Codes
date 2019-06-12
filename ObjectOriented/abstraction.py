#Abstraction is not a default object oriented programming features in python
#Abstraction is the object oriented principle,It is used to create an interface to all subclasses
#abstract method is implemented in the  the abstrat baseclass and defined in the subclasses
#we cannot instantiate object for parrent classes

#we can hide the necessory functionalites of class from user .This is known as abstraction
#That means showing only necessory functionalites to the user
#In simple,Abstract base class creates the interface to the user hidding necessary info.


from abc import ABC,abstractmethod
#This is the abstract base class
class Computer(ABC):
	@abstractmethod
	def compute(self):
		pass
	@abstractmethod
	def specification(self):
		pass



#This is the concrete class inheriting ABC class
class Os(Computer):
	def compute(self):
		print('Computing Os...........')
	def specification(self):
		print('Linux os............')

#This is concrete class inheriting ABC class
class Software(Computer):
	def compute(self):
		print('Computing Software............')

	def specification(self):
		print('Scrapy framework.............')




# computer=Computer()
os=Os()
software=Software()
os.compute()
os.specification()
software.compute()
software.specification()
