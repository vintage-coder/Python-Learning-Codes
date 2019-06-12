__author__='gowthaman'

import random 

#Bubble sort Algorithm
#This approach based on the function

b=[i for i in random.sample(range(5,150),20)]

print("The list is:",b)
n=len(b)


def bubblesort(a):
	
		for k in range(n-1):
			flag=0
			for i in range(n-k-1):
				if a[i]>a[i+1]:
					a[i],a[i+1]=a[i+1],a[i]
					flag=1
			if flag==0:
				break
bubblesort(b)
print("The list is:",b)
print("largest:",b[n-1])

#This approach based on the object oriented


#Best Case:O(n)
#Average Case:O(n2)
#worst case:O(n2)


class Bubble:

	def __init__(self):
		self.number=[k for k in random.sample(range(5,25),20)]
		self.length=len(self.number)

	def sorting(self):
		for k in range(self.length-1):
			flag=0
			for i in range(self.length-k-1):
				if self.number[i]>self.number[i+1]:
					self.number[i],self.number[i+1]=self.number[i+1],self.number[i]
					flag=1
			if flag==0:
				break
	def display(self):
		print("The list before sorting:",self.number)
		self.sorting()
		print("The list after sorting:",self.number)


obj=Bubble()

obj.display()
