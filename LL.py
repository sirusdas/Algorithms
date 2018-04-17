#FileName: LL.py
#Creator: Sirus Das
from node import node

class LL(object):
	def __init__(self):
		print("\nWelcome to LinkedList Example.\n")
		self.head = None
		self.counter = 0

	def traverseList(self):
		if self.head is not None:
			print("\nCurrent Linked List Values:")
		else:
			print("\nLinked List empty")
			
		actualNode = self.head; #Assiging Start Node obj to actualNode obj

		while actualNode is not None:
			print (actualNode.data);
			actualNode = actualNode.nextNode #nextNode is an object

	def insertStart(self, data):
		print("Inserting Value {} at the start of LL".format(data))
		self.counter = +1
		newNode = node(data)

		if not self.head: #i.e if head is None go into this loop
		    #Called on the initial kick!
		    self.head = newNode

		else:
		    newNode.nextNode = self.head
		    self.head = newNode #swapping and storing the current node as head
		

	def size(self):
		return self.counter;

	def insertEnd(self, data):
		if self.head is None:
			print("\nLinked list empty. Please insert at the start")
			return 0
		print("Inserting Value {} at the end of LL".format(data))
		newNode = node(data)
		actualNode = self.head

		while actualNode.nextNode is not None: #reach the end of linked list
			actualNode = actualNode.nextNode;

		actualNode.nextNode = newNode; #Inserting the value!
		

	def remove(self, data):
		if self.head is None or self.head.nextNode is None:
			print("\nLinklist is Empty")
			return 0
			
		print("\n...initializing to remove ",data)
		if self.head:
			if data == self.head.data: #this is the initial or first node
				print("...removing ",data)
				self.head = self.head.nextNode
			else: #other than the first node
				self.head.remove(data, self.head)
				#this will give calls to node class > remove method

