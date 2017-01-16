'''Single Linked List - means that the nodes point only to the successor 
	(no predecessor)
'''

class LinkedList(object):

	def __init__(self):
		self.len = 0
		self.head = Node()

	def insert(self,data):
		self.head.insert(data)
		self.len += 1

	def search(self,data):

		return self.head.search(data)

	def delete(self,data):

		success = self.head.delete(data)
		if success == True:
			self.len -= 1
		return success


class Node(object):

	def __init__(self, data = None):

		self.data = data
		self.next_node = None

	def insert(self,data):

		if self.data == None:
			self.data = data
			self.next_node = Node()
		else:
			self.next_node.insert(data)

	def search(self,data):

		if self.data == data:
			return self
		elif self.next_node == None:
			return False
		else:
			return self.next_node.search(data)


	def delete(self,data):
		''' O(n) - because you have to traverse the whole list if the data is in the last node 
			
		'''
		if self.search(data):

			if self.data == data:
				self.data = self.next_node.data
				self.next_node = self.next_node.next_node
			else:
				self.next_node
		else:

			return False
		return True

	def __str__(self):
		return str(self.data)
