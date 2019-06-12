__author__ = "gowthaman"
class Node:
	def __init__(self,dataField=None):
		'''This is Node constructor method'''
		self.dataField=dataField
		self.nextField=None

#This is the single linked list class

class SingleLinkedList:
	def __init__(self):
		self.headval=None

	def list_length(self):
		printval=self.headval
		count=0
		while printval is not None:
			printval=printval.nextField
			count+=1

		return count

	def __sizeof__(self):
		return self.list_length()


	def insert_at_begining(self,data):
		print("inserting {} at the begining of the node".format(data))
		NewNode=Node(data)
		NewNode.nextField=self.headval
		self.headval=NewNode

	def insert_at_end(self,data):
		print("inserting {} at the end of the node".format(data))
		NewNode=Node(data)
		printval=self.headval
		while printval.nextField:
			printval=printval.nextField
		printval.nextField=NewNode


	def remove_node(self,key):
		printval=self.headval
		print("Removing {} in the list".format(key))
		while printval is not None:
			if printval.dataField==key:
				printval=printval.nextField
				prev.nextField=printval
				break
			
			prev=printval
			printval=printval.nextField
			

	def insert_inbetween_node(self,middle_node,data):
		NewNode=Node(data)
		print("inserting {} after {} in the list".format(data,middle_node))

		if middle_node is None:
			print("The node is absent")
		printval=self.headval
		while printval is not None:
			if printval.dataField==middle_node:
				NewNode.nextField=printval.nextField
				printval.nextField=NewNode
				break

			printval=printval.nextField


	def display_nodes(self):
		printval=self.headval
		print("Listing the nodes in the list")
		while printval is not None:
			print(printval.dataField,end="==>")
			printval=printval.nextField
		print("")




obj=SingleLinkedList()
obj.headval=Node("1")
data1=Node("2")
data2=Node("3")
data3=Node("4")
obj.headval.nextField=data1
data1.nextField=data2
data2.nextField=data3


if __name__=="__main__":
	obj.display_nodes()
	
	obj.insert_at_begining("20")
	obj.insert_at_end("100")
	obj.display_nodes()
	print("The length of the list is {}".format(obj.list_length()))
	obj.insert_inbetween_node("2","vasu")
	obj.display_nodes()
