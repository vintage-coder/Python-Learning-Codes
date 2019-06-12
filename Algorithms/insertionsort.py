import random
#This is the insertion sort Algorithm
a=[i for i in random.sample(range(20,100),20)]
b=[i for i in random.sample(range(20,100),20)]


print("The list {} and length {} ".format(a,len(a)))


def insertion(a_list):
	for index in range(1,len(a_list)):
		
		while index>0 and a_list[index-1]>a_list[index]:
			a_list[index-1],a_list[index]=a_list[index],a_list[index-1]
			index-=1

if __name__=='__main__':
	insertion(a)

	print('The sorted list {} and length {}'.format(a,len(a)))


#The class implementation of insertion sort Algorithms

class Insertion:
	def __init__(self,lists):
		self.lists=lists
		print('The list {} and length is {}'.format(self.lists,len(self.lists)))

	def sort(self):
		for index in range(1,len(self.lists)):
				while index>0 and self.lists[index-1]>self.lists[index]:
					self.lists[index],self.lists[index-1]=self.lists[index-1],self.lists[index]
					index-=1

	def print_list(self):
		print('The sorted list {} and length is {}'.format(self.lists,len(self.lists)))		



if __name__=='__main__':
	obj=Insertion(b)
	print('sorting.....')
	obj.sort()
	print('Sorting completed........')
	obj.print_list()


#Another way of implementation of insertion sort


def insertion(a_list):
	for i in range(1,len(a_list)):
		key=a[i]
		position=i
		while position>0 and a[position-1]>key:
			a[position]=a[position-1]
			position-=1
		a[position]=key

	
if __name__=='__main__':
	print('The list {} and length is {}'.format(a,len(a)))
	insertion(a)
	print('The sorted list {} and length is {}'.format(a,len(a)))
