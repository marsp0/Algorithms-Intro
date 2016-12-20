class Stack(object):

	def __init__(self):

		self.top = Node()
		self.size = 0

	def push(self, data):
		if self.top.data == None:
			self.top.data = data
		else:
			temp_node = self.top
			self.top = Node(data)
			self.top.next_node = temp_node
		self.size += 1

	def pop(self):
		if self.is_empty():
			return False
		else:
			to_pop = self.top.data
			if self.top.next_node != None:
				self.top = self.top.next_node
			else:
				self.top = Node()
		self.size -= 1
		return to_pop

	
	def traverse(self):
		counter = self.size
		current = self.top
		while counter > 0:
			print current.data
			current = current.next_node
			counter -= 1

	def is_empty(self):
		return self.size == 0



class Node(object):

	def __init__(self,data = None):

		self.data = data
		self.next_node = None

	
if __name__ == '__main__':

	stack = Stack()
	for i in xrange(10):
		#print i
		stack.push(i)
	stack.traverse()