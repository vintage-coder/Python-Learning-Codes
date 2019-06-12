#Singleton pattern using the __new__ method  by overridding the object class

class Singleton(object):
	_instance=None

	def __new__(cls):
		if Singleton._instance is None:
			Singleton._instance=super().__new__(cls)
		return Singleton._instance


obj1=Singleton()
obj2=Singleton()
obj3=Singleton()

assert obj1 is obj2 is obj3

print('Singleton was created...')


#Singleton Design pattern using inheritance


class Singleton(object):
    def __new__(gow):
        if not 'instances' in gow.__dict__:
                gow.instances=object.__new__(gow)
                print('The instance is:',gow.instances)
        return gow.instances

class gowtham(Singleton):#In this case the custom class is passed to the argument of singleton class to make singleton behaviour
    pass 	#when we creating the object to this class the __new__ method is automatically called before instantiation

# obj1=gowtham()  #In this case the making of singleton class using custom concrete class
# obj2=gowtham()  #indirect calling of superclass ,that is by inheriting the behaviour of super class

obj4=gowtham()
obj5=gowtham()
assert obj4 is obj5
print('instantiation indirectly',obj4)
print('instantiation indirectly',obj5)
obj1=Singleton() #making of singleton using type class 
obj2=Singleton() #OR direct calling of superclass
obj3=Singleton() #Here instantiation occurs directly by super class
print('instantiation directly',obj3)

#Note:#Direct and indirect instantiation will always be different
assert obj1 is obj2 is obj3
print('This is a singleton pattern..... $')


#Singleton Design pattern by another instance of class

#Note:This below class create Singleton object for gowtham i.e only creates gowtham object
#so we cannot see the singleton instances obj1._instance gives an error because gowtham doesnot have 'attribute'

class Singleton:
    _instance=None

    class gowtham:
        pass
    def __new__(cls):
        print('The class is:',cls)
        if Singleton._instance is None:
            Singleton._instance=Singleton.gowtham()
        return Singleton._instance

obj1=Singleton()
obj2=Singleton()
obj3=Singleton()

assert obj1 is obj2 is obj3
print('This is a singleton pattern')


#Singleton Design pattern and Limiting  instance creation

#we can also limit the instance creation using singleton class
#in this singleton class only 3 instance can be made after that last instance is repeated

class Singleton:
	count=0
	_instance=None
	def __new__(cls,*args,**kwargs):
		
		if Singleton.count<=2:
			Singleton._instance=super().__new__(cls,*args,**kwargs)
		Singleton.count+=1
		return Singleton._instance

class gowtham(Singleton):
	pass

obj1=gowtham()
obj2=gowtham()
obj3=gowtham()
obj4=gowtham()


#Singleton Design pattern and randomly selecting instance from the list


#In this singleton example the 3 instance are instantiated after that the random instance is 
#selected from already created instance

import random
class Singleton:
	_instance=[] #This list stores all the instances already created
	count=0
	def __new__(cls,*args,**kwargs):
		if Singleton.count<=2:
			instance=super().__new__(cls,*args,**kwargs)
			Singleton._instance.append(instance)
			Singleton.count+=1
			return instance
		else:
			return random.choice(Singleton._instance)


class gowtham(Singleton):
	pass


obj1=gowtham()
obj2=gowtham()
obj3=gowtham()
obj4=gowtham()


#Singleton Design pattern using metaclass



#The below class is the meta class.It will act as a meta class

#in normal case (on concrete class)
#type(obj)--->class name-->type(class name)-->type class(default metaclass)

#in custom meta class
#type(obj1)---->MyClass name-->type(MyClass name)--->MetaSingleton(it is custom metaclass )--->type(MetaSingleton)--->type class(default metaclass)

#in general custom metaclass means creating an extra layer below the type class and it will act as a cutom metaclass

class MetaSingleton(type):
    _instances = {}
    def __call__(self, *args, **kwargs):#In this __call__ method 'self' instance is not created yet,self args is class passed to meta class
        if self not in self._instances: #__call__ method can take "(class or instance)"
            self._instances[self] = super().__call__(*args, **kwargs)
            print("The instance is:",self._instances[self])
       
        return self._instances[self]#In this program better way is cls instead of self

class SingletonMixin(metaclass=MetaSingleton): #here the magic happens
#it act as a abstraction layer
    
    pass
class MyClass(SingletonMixin):#This class invoke directly the MetaSingleton class not SingletonMixin

    pass

obj1 = MyClass()
obj2 = MyClass()


assert obj1 is obj2

obj3=SingletonMixin()
obj4=SingletonMixin()

print("There is no error")


