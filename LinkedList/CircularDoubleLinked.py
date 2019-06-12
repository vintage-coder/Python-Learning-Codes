class Node:
	def __init__(self,data,next=None,prev=None):
		self.data=data
		self.next=None
		self.prev=None


class CircularDoubleLinkedList:
	def __init__(self):
		self.headval=None

	def __repr__(self):
		return str("CircularDoubleLinkedList")

	def insert_at_begining(self,data):
		print("Insert {} at the begining of the nodes".format(data))
		NewNode=Node(data)
		if self.headval==None:
			self.headval=NewNode
		else:
			printval=self.headval
			NewNode.next=printval
			printval.prev=NewNode
			self.headval=NewNode

		

	def insert_at_end(self,data):
		NewNode=Node(data)
		printval=self.headval
		while printval is not None:

			previous=printval
			printval=printval.next
		previous.next=NewNode
		NewNode.prev=previous




	def display_nodes(self):
		printval=self.headval
		print("Displaying the nodes in the list")
		while printval is not None:
			print(printval.data,end="<===>")
			printval=printval.next
		print("")




obj=CircularDoubleLinkedList()
obj.headval=Node("Apple")
data1=Node("Banana")
data2=Node("Cherry Fruit")
data3=Node("Dragen Fruit")
obj.headval.next=data1
data1.prev=obj.headval
data1.next=data2
data2.prev=data1
data2.next=data3
data3.prev=data2


if __name__=="__main__":
	obj.display_nodes()
