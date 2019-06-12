#inheritance is one of the feature of the object oriented programming
#some or All of the features of parrent class can be reused in child class 
#This is the use of inheritance
#we can reuse the properites like attribute and behaviour of the parrent class in child class

#Single Inheritance

# This is parrent
class Father:
	def __init__(self,name,age):
		self.__name=name
		self.__age=age
	

	def __str__(self):
		return self.__name

	def print_father_name(self):
		print('The Father name is {}'.format(self.__name))


	def print_father_age(self):
		print("The Father age is  {}".format(self.__age))


#This is Child Class
class Son(Father):
	#This is initialisation of constructor method
	def __init__(self,name,age,degree):
		super().__init__(name,age)
		Father.__init__(self,name,age)
		
		self.degree=degree

	#This is instance method
	def print_son_name(self):
		print('The name of son is {} '.format(self._Father__name))

	def print_son_age(self):
		print('The age of son is {age}'.format(age=self._Father__age))

	def print_son_degree(self):
		print('The degree of son is %s'%self.degree)


father=Father("Sivan",55)
son=Son("Murugan",18,'Electronics')
# father.print_name()
son.print_son_name()
son.print_son_age()
son.print_son_degree()
father.print_father_name()
father.print_father_age()

#Multiple inheritance

class Honda:
	def __init__(self,name,color,price):
		self.name=name
		self.color=color
		self.price=price

	def print_details(self):
		print('The name of car is %s'%(self.name))
		print('The color of car is {}'.format(self.color))
		print('The price of car is',self.price)


class Maruthi:
	def __init__(self,brand):
		self.brand=brand

	def print_details(self):
		print('The brand name is {}'.format(self.brand))

class TATA:
	def __init__(self,country):
		self.country=country


	def print_details(self):
		print('The country of manufacturing is {}'.format(self.country))


#This child class inherits features from three parrent class

class Car(Honda,Maruthi,TATA):
	def __init__(self,name,color,price,brand,country):
		super().__init__(name,color,price)
		Maruthi.__init__(self,brand)
		TATA.__init__(self,country)

	def print_details(self):
		super().print_details()
		Maruthi.print_details(self)
		TATA.print_details(self)



car=Car("Audi","Silver",20000,"Top","Germany")

car.print_details()

