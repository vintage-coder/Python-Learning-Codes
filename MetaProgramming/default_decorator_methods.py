#This is static decorator method which is used to define a method without passing the object
#It is declared inside the class using the @staticmethod sytax


class Example:
	
	#staticmethod not bound to object eventhought calling via object or class
	a=10
	b=20
	@staticmethod
	def get_item():
		print('This is the static method')

	def normal_item(self):
		print('This is the normal instance method')
		print('Instance method :',self.a,self.b)
	#classmethod is a bound method we can call normal as normal method
	@classmethod
	def class_item(cls):
		print('This is the class method')

obj=Example()

# print(Example.get_item)
# Example.get_item()
# print(obj.get_item)
# obj.get_item()

#classmethod
print(Example.a)
print(obj.a)
# print(Example.class_item)
# Example.class_item()
# print(obj.class_item)
# obj.class_item()
