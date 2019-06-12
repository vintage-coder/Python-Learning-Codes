#Python tricks
class gowtham:
	pass

#creating class method outside of the class
gowtham.acting=lambda a:print('This is the class method')

gowtham.age=23

print(gowtham.age)
print(gowtham.acting('hi')) #This is the one way of calling anonymous function

obj=gowtham()

obj.acting()
