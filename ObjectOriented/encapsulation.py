#Encapsulation is another Features of object oriented programming laguage
#it encapsulates the attributes and behaviours inside the class(privatisation of attributes)
##It is default feature of OOPs
# we can restrict access from user being invoked the methods and varibles

class Car:

	__name=" "
	def __init__(self):
		self.__engine_started()
		#This is private variable or attribute
		self.__name="Audi"
		self._engine="hp600" #single under score defines that attribute only for internal use
							 #This wonot affect anything in class inside or outside
	#This method starting with __ will work only in inside of the class
	#Because,this method mangling with class name
	#This method is a.k.a private method
	def __engine_started(self):
		self._keyInserted()
		print("{} Engine starting......".format(self._engine))

	def _keyInserted(self):
		print("key inserted..........")

	#This is instance method
	def acceleration(self):
		print('Acceration was given.',self.__name)


	def setAttribute(self,name):
		self.__name=name


car=Car()
car.acceleration()


#Eventhough we can access that method using car._Car__engine_started()
#It will give the output,It privates accidently modifying the variable


#This is the one of best example of encapsulation
class Bird:
	def __init__(self):
		self.__name="kukoo"

	def setName(self,name):
		self.__name=name

	def displayName(self):
		print("The name of the bird is:",self.__name)


obj=Bird()
obj.displayName()
obj.__name="Peacock" #this Wonot affect the self.__name inside of the class,Outside of the class
#The mangling of private variable changes the attribute
obj.displayName()

#This problem can be overcome by the setter func
obj.setName("Peacock")
obj.displayName()

