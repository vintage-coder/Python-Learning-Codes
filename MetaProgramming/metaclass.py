#Main motive of metaprogramming is "Donot repeat yourself".
#This means that programmers should not repeat the code . They should reuse the code
#The primary goat of metaprogramming is to manipulate the code by modifying,wrapping and generating the 
#existing code
#Three major features of metaprogramming is :
	#1.Decorators
	#2.Class Decorators
	#3.MetaClasses



#Metaprogramming is simply the code that manipulates the codes

#MetaClass
#The default metaclass is type class
#The default base class is object class

#we can create our own metaclass my overridding the type class and thus creating custom base class
#This base class is spread to all classes when classes are created,By thus,we can control 
#The creation of classes

#This is our custom meta class overridden from the type class
class CustomMeta(type):
	_instances=None
	
	#This method is accessible to all derived class
	def gowtham(cls):
		print('The classname is:',cls)
		print('This is the default method accessible to all derived classes')

	def __new__(cls,classname,bases,clsdict):
		print('The metaclass name:',cls)
		print('The class name:',classname)

		#Controlling the base classes inheriting more than one bases
		if len(bases)>1:
			raise TypeError('Cannot inherit more than one class')

		#The class is returned by overridding the type class
		class_created=super().__new__(cls,classname,bases,clsdict)

		return class_created


	def __init__(cls,classname,bases,clsdict):
		print('The metaclass name __init__ method:',cls)
		print('The classname __init__ method:',classname)
		print('The base classname __init__ method',bases)
		print('The class dict __init__ method',clsdict)

	#Limiting the instance creation to one instance by overridding the call of method
	def __call__(cls,*args,**kwargs):
		if CustomMeta._instances is None:
			CustomMeta._instances=super().__call__(*args,**kwargs)
		print('The created instance is:',CustomMeta._instances)
		setattr(CustomMeta._instances,'gowtham',cls.gowtham)
		return CustomMeta._instances




#This is our custom baseclass it is propagated to all level of hierarchy of derived class
#This is the base class
#This metaclass is automatically called when we create class
class CustomBase(metaclass=CustomMeta):
	pass



#This is the drived class ,It is derived from the custom base class
# class gowtham(CustomBase):
# 	pass

#This is also drived class,derived from custom base class
# class pythonist(CustomBase):
# 	pass




#The simple explanation how class is created in python using type class

# def getdata(self,value):
# 	print('The value got by the method is:',value)

# classref=type('MyClass',(list,),dict(name='gowtham',data=getdata)) #This is the class creation sytax

#Here the type is the default metaclass and its default base class is object
#and we can also pass the attributes values and methods are passed
#The MyClass is created and assigned to the variable name classref

# obj=classref() #instance is created to MyClass

#object is the class which is the base class to all custom class creation

#Like above when we create a custom concrete class ,class name,attributes,methods are passed to type class to create the class

#Thus from the above perspective,The type class is overridden to create type metalcass
#by using the custommeta class we can control the class creation and many more activites
#can be done.



#we cannot see the memory address of default class like list,dict,int,bool etc..
#we can see only the custom concrete class memory address

































#type class contains all instance to create a normal class,we can create a our own class using metaclass 
#By overriding type class

# class gowtham:
# 	def __init__(self,name=None):
# 		self._name=name
# 		self._age=30

# 	@property
# 	def name(self):
# 		print('Get attribute is invoking')
# 		return self._name

# 	@name.setter
# 	def name(self,value,age):
# 		print('Setting attribute invoking')
# 		self._name=value
# 		self._age=age
# 		return self._name,self._age

# 	@name.deleter
# 	def name(self):
# 		print("deletter attribute invoking")
# 		del self._name


