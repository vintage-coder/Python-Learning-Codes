import random
class gowtham:
		instances=[]
		def __new__(cls,*args,**kwargs):
			if len(gowtham.instances)<3:

				data=super().__new__(cls)
				gowtham.instances.append(data)
				return data
			else:
				return random.choice(gowtham.instances)




