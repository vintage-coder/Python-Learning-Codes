#object is the instance of class.Class is the blue print of object or instance
#With out object or instance the class is inactive that means we cannot call the methods of
#The class with out object.
#we can create many instance for a particular class. Each instance behave or hold the 
#different instance varible values but the class varible value is same for multiple instances
#but we can change the class variable values by calling each time
#The main concept of oops is reusability.That means Donot repeat yourself(DRY)

#A Single custom class
class Car:
	no_of_items=0
	__speed=500

	#initialization or constructor
	def __init__(self,name,color):
		self.name=name
		self.color=color
		self.__speed=Car.__speed

	#This is instance method
	def print_details(self):
		Car.no_of_items+=1    #The value of class args updated when each time instance method is called using 
		#different instances
		print("The call of count is",self.no_of_items)
		print('The color of car is :',self.color)
		print("The name of car is :",self.name)

	def setSpeed(self,speed):
		self.__speed=speed

	def accelerate(self,speed):
		self.__speed+=speed

	def display(self):
		print('the current speed is:',self.__speed)

obj1=Car("Audi","Black")#First instance
obj2=Car("BMW","White")#Second instance

obj1.print_details()
obj2.print_details()
obj1.accelerate(200)
obj1.display()
obj2.__speed=0  # Not possible because of the name mangling for only accidently changing value
obj2.display()
