 #Method overloading is a features of object oriented programming language.it is
 #the subset of polymorphism that means it takes various forms of representation
#Method overloading is not performed in python unlike any other programming languages
#like c,c++ etc. Eventhough we can solve different approach to solve method overloading''

def addition(a,b,c):
	return a+b+c

def addition(a,b):
	return a+b

#This function will give the result
print(addition(12,13))
#This function call wonot give result,because the the first three argument addition function
#is replaced by two argument additon funtions.so it will give the error
# print(addition(11,23,10))

# #we can solve this problem another way
def addition(instance,*args):
	if instance=="int":
		result=0
	elif instance=="str":
		result=''
	else:
		pass
	for i in args:
		result+=i
	return result


print("Addition is",addition("int",1,2,3,9,8)) #This is five argument funtion call
print("Addition is",addition("int",3,4,5,6,7,7,8))#This is the seven argument same funtion call
print("String concatination is:",addition("str","hi ","gowtham ","how ","are you?"))
#Thus we can achive the method overloading
#another method 

#This is the class implementation of addition
class Addition:
	#This is method depicts the method overloading func.That is,we can pass two,three args
	def addition(self,a,b,val=None):
		if val is not None:
			result=a+b+val
		else:
			result=a+b

		return result
obj=Addition()
print('The addition is',obj.addition(45,67,21))#Three argument are passed
print('The addition is',obj.addition(24,25))#Two args are passed to the same function



