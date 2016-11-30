class Stack(object):

	def __init__(self):

		self.top = Node()

	def push(self, data):
		new_top = Node(data)
		new_top.next_node, self.top = self.top, new_top
		
	def pop(self):

		to_pop, self.top = self.top, self.top.next_node
	
	def traverse(self):
		pass



class Node(object):

	def __init__(self,data = None):

		self.data = None
		self.next_node = None

	
if __name__ == '__main__':
	