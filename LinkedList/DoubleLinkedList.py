class Node:
	def __init__(self,data,next=None,prev=None):
		self.data=data
		self.next=None
		self.prev=None


class DoublyLinkedList:
	def __init__(self):
		self.headval=None

	def list_length(self):
		printval=self.headval
		count=0
		while printval is not None:
			count+=1
			printval=printval.next
		return count

	def __repr__(self):
		return str("DoublyLinkedList")

	def __sizeof__(self):
		return self.list_length()

	
	def insert_at_begining(self,data):
		print("inserting {} at the begining of node".format(data))
		NewNode=Node(data)
		printval=self.headval
		NewNode.next=printval
		printval.prev=NewNode
		self.headval=NewNode

	def insert_at_end(self,data):
		print("inserting {} at the end of nodes in the list".format(data))
		NewNode=Node(data)
		printval=self.headval
		while printval is not None:
			previous=printval
			printval=printval.next

		previous.next=NewNode
		NewNode.prev=previous

	

	#This is the reversing of nodes in the list
	def reverse_nodes(self):
		tmp=None
		cur=self.headval
		while cur:
			tmp=cur.prev
			cur.prev=cur.next
			cur.next=tmp
			cur=cur.prev
		if tmp:
			self.headval=tmp.prev

	def remove_nodes(self,key):
		printval=self.headval
		print("Removing {} nodes in the list".format(key))
		
		while printval is not None:
			if printval.data==key:
				temp=printval.next
				previous.next=temp
				temp.prev=previous
				break
			previous=printval
			printval=printval.next



	def display_nodes(self):
		printval=self.headval
		print("Displaying the node in the list")
		while printval is not None:
			print(printval.data,end="<==>")
			printval=printval.next
		print("")

	def insert_inbetween_node(self,middle_node,data):
		print("insert {} after the {}".format(data,middle_node))
		NewNode=Node(data)
		printval=self.headval
		while printval is not None:
			if printval.data==middle_node:
				nextField=printval.next
				printval.next=NewNode
				NewNode.prev=printval
				NewNode.next=nextField
				nextField.prev=NewNode
				break
			printval=printval.next




obj=DoublyLinkedList()

obj.headval=Node("gowthaman")
data1=Node("anbarasan")
data2=Node("amuthan")
data3=Node("ganesh")

obj.headval.next=data1
data1.prev=obj.headval
data1.next=data2
data2.prev=data1
data2.next=data3
data3.prev=data2


if __name__=="__main__":
	obj.display_nodes()
