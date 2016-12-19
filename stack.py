class Stack(object):

	def __init__(self):

		self.top = Node()
		self.size = 0

	def push(self, data):
		new_top = Node(data)
		new_top.next_node, self.top = self.top, new_top
		self.size += 1

	def pop(self):
		to_pop, self.top = self.top, self.top.next_node
		self.size -= 1
	
	def traverse(self):
		pass

	def is_empty(self):
		return self.size == 0



class Node(object):

	def __init__(self,data = None):

		self.data = None
		self.next_node = None

	