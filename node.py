#FileName: node.py
#Creator: Sirus Das
#Desc: This the basic frame work for any node!
class node:

	def __init__(self, data):
		self.data = data
		self.nextNode = None;
		
		
	'''
	Working:
		Every Node object we create will have data and next node with it.
		While a remove is initiated,
			the "previousNode" is always the 1st node in the Linked List.
			Which ever method calls this remove it will first check if the first element
			is not the requested element to remove. If it is then remove it there itself else 
			give a call to this remove method referencing the firstNode as previousNode.			
	'''
	def remove(self, data, previousNode):
		print("Found Value {}".format(self.data))
		if self.data == data:
			print("...removing ",data)
			previousNode.nextNode = self.nextNode;
			del self.data;
			del self.nextNode;
		else:
			if self.nextNode is not None:
				#print("Found Value {}".format(self.nextNode.data))
				self.nextNode.remove(data, self)
				#in the above code self will have the object of self.nextNode
		