

def timer(func):
	print('The class name is:',func)
	def wrapper(*args,**kwargs):
		print('The args and kwargs are:',args,kwargs)
		result=func(*args,**kwargs)
		print('The color is:',result.getColor())
		return result
	return wrapper


@timer
class Flower:
	def __init__(self,name,color):
		self.name=name
		self.color=color

	def getColor(self):
		print('The color of Flower is:',self.color)




















# class test():
#     def __init__(self,func):
#         print("__init__() method")
#         self.func=func
#         print('Directory values are:',dir(self.func))
#         print("values of func is and name",func,func.__name__)
        

#     def __call__(self,*args):
#         print('arguents are:',args)
#         print("inside __call__()")
#         self.func(*args)
#         print("After __call__()")



# @test   #This is a class decorator.class takes the function as a argument and 
# def gowthaman(a,b,c):# The function arg
#     print("values are:",a,b,c)

# print('=============')
# gowthaman("hi","gowtham","how are you?")
# print("----------------")

# gowthaman(1,2,3)  #fucntion calling is like object calling ,the arguments are go to __call__ method
#function is directly passed to the class directly using class decorator