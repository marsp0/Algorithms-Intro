class Tree(object):

	def __init__(self):
		
		self.root = Node()

	def insert(self,data):




class Node(object):

	def __init__(self,data = None, parent = None):

		self.parent = None
		self.data = data
		self.left = None
		self.right = None

	def insert(self,data):

		if self.data === None:

			self.data = data
		else:
			if data < self.data:
				if self.left == None:
					self.left = Node(data,self)
				else:
					self.left.insert(data)
			else:
				if data > self.data:
					if self.right == None:
						self.right = Node(data,self)
					else:
						self.right.insert(data)

	def delete(self,data):

		if self.data == data:

			if self.right == None and self.left == None:

				if self.parent.left.data == data:

					self.parent.left = None
				else:

					self.parent.right = None
			elif self.right == None or self.left == None:

				if self.right == None:

					self.data , self.left = self.left.data , self.left.left
				
				else:

					self.data, self.right = self.right.data , self.right.right

			else:

				counter = self.right
				while True:
					if self.right = None:
						break
					else:
						counter = counter.right

				self.data = counter

		else:
			if data < self.data:
				self.left.delete(data)
			else:
				self.right.delete(data)
		

	def search(self,data):

		if self.data == data:
			return self.data
		else:
			if data < self.data:
				return self.left.search(data)
			else:
				return self.right.search(data)
