#Dunter method is also known as magic method
__author__="Gowthaman"

class Magic:

	def __new__(cls,*args,**kwargs):
		obj=super().__new__(cls)
		print('The arguments are:',args)
		print('The keyword arguments are:',kwargs)
		print('The created instance is :',obj)
		return obj


	def __init__(self,age,name):
		self.age=age
		self.name=name
		self.val=["apple","orange","mango","pine apple"]

	def __repr__(self):
		"""Representation of class """
		return "Rep Items:{!r}{!r}".format(self.name,self.age)
	def __str__(self):
		"""String representation of object"""
		return "Str Itmes:{!s}{!s}".format(self.name,self.age)
	def __call__(self):
		"""Calling the object Magic method"""
		return self.__dict__


	def __add__(self,other):
		"""This is the add dunter method for object addition"""
		result=None
		a_instance=(int,str,float)
		if hasattr(other,'age'):
			result=self.age+other.age
		elif isinstance(other,a_instance):
			result=self.age+float(other)

		return result

	def __lt__(self,other):
		"""checking for less than comparision of object"""
		result=None
		a_instance=(int,str,float)
		if hasattr(other,'age'):
			result=self.age<other.age
		elif isinstance(other,a_instance):
			result=self.age<float(other)

		return result


	def __le__(self,other):
		"""Checking for less than or equal to comparision of object"""
		result=None
		a_instance=(int,str,float)
		if hasattr(other,'age'):
			result=self.age<=other.age
		elif isinstance(other,a_instance):
			result=self.age<=float(other)

		return result


	def __gt__(self,other):
		"""Checking for greater than comparision of object"""
		result=None
		a_instance=(int,str,float)
		if hasattr(other,'age'):
			result=self.age>other.age
		elif isinstance(other,a_instance):
			result=self.age>float(other)
		return result


	def __ge__(self,other):
		"""Checking for greater than or equal to comparision of object"""
		result=None
		a_instance=(int,str,float)
		if hasattr(other,'age'):
			result=self.age>=other.age
		elif isinstance(other,a_instance):
			result=self.age>=float(other)

		return result
	
	def __eq__(self,other):
		"""This is the equal dunter method compares object of the class with other items"""
		result=None
		instances=(int,str,float)
		if hasattr(other,'age'):
			result=self.age==other.age
		elif isinstance(other,instances):
			result=self.age==int(other)
		return result


		return self.age==other.age

	def __ne__(self,other):
		"""This is the not equal to dunter method.It return true of object is not equal to comparable object"""
		result=None
		instances=(int,str,float)
		if hasattr(other,'age'):
			result=self.age!=other.age
		elif isinstance(other,instances):
			result=self.age!=float(other)
		return result

	
	# def __getattribute__(self,name):
	# 	if name in self.__dict__:
	# 		return self.__dict__[name] 


	def __getattr__(self,key,value=None):
		if key is None:

			if key in self.__dict__:
				return self.__dict__[key]
			else:
				return value
		else:
			if key in self.__dict__:
				return self.__dict__[key]
			else:
				pass
	def __hasattr__(self,key):
		"""This method is used to check whether the object has the attribute or not"""
		if key in self.__dict__:
			return True
		else:
			return False
	def __setitem__(self,key,value):
		"""This method is used to set the value to the given key"""
		if self.__dict__.get(key,None) is None:
			self.__dict__[key]=value
		elif key in self.__dict__:
			self.__dict__[key]=value
	
	def __getitem__(self,key):
		"""This is for getting the value from the dictionary"""
		return self.__dict__.get(key,None)

	def __delitem__(self,key):
		"""This delitem method removes the attribute of desired class"""
		if key in self.__dict__:
			del self.__dict__[key]
	def __iter__(self):
		"""This dunter method allows to iter the object in the dictionary"""
		for i,j in self.__dict__.iteritem():
			yield i,j

	def __contains__(self,key):
		"""This is used to check wheather the element is present or not"""
		return key in self.__dict__
		



		
if __name__=='__main__':
	
	print("The author is :",__author__)
	obj1=Magic(18,'anbarasan')
	obj2=Magic(23,'Gowthaman')
	print("The Representation of object {!r}".format(obj1))
	print("The Representation of string object is {!s}".format(obj1))
	class_name=obj1.__class__.__name__
	print('The class name is:',class_name)
