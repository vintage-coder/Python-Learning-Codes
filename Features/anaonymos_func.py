#Anonymous function is the special function in python.It will take any no of args but ,it
#Must have only one expression
#Anonymous function simplifies the expression.It powers up the code when we use 
#inside the function
#the evaluated expression is returned back
#Anonymous function is the function defined without function name.
#it is defined using the keyword lambda
#lamda functions is used along with fiter(),map() mostly.

y=lambda m,x:m*x+7

print(y(0.5,6))
print(y(12.6,17))

#defining anonymous funtion inside the function
def function(n):
	return lambda a:a*n

double=function(2)
triple=function(3)

print("doubling value:",double(15))
print("tripling value:",triple(18))


#Filter function

#filter function filters the list based on the if the return value is True from the anonymous function
x=[i for i in range(20)]#List comprehension
y={i for i in range(20)} #Set comprehension
z={i:i+2 for i in range(20)}#Dictionary comprehension
w=(i for i in range(20)) #Generators creation

#The below fuction filter the even value from the list
new_list=list(filter(lambda x:(x%2==0),x))

print('The even value from the list is :',new_list)

new_list=list(filter(lambda x:(x%2==1),x))

print('The odd value from the list is:',new_list)


#Map function

#map funtion,evaluate all the items in the list and returns back.simply,it maps every
#item in the list and process in the function and return back

new_list=list(map(lambda x:0.7*x+21,x))

print('The evaluated expression by map and lambda function is ',new_list)


#Reduce funtion 
#It was removed from python 3 however it is available in functools library
#just import that "from functools import reduce"

from functools import reduce
#it will calculate the sum of all elements in the list
new_list=reduce(lambda x,y:x+y,x)

print("The sum of the list in the list is",new_list)

