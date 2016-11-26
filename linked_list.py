class LinkedList(object):

	def __init__(self):
		self.len = 0
		self.current_node = Node()

	def insert(self,element):
		self.current_node.insert(element)
		self.len += 1

	def print_elements(self):
		
		self.current_node.print_element()



class Node(object):

	def __init__(self, current = None):

		self.current_node = current
		self.next_node = None

	def insert(self,element):

		if self.current_node == None:
			self.current_node = element
			self.next_node = Node()
		else:
			self.next_node.insert(element)

	def print_element(self):

		print self.current_node

		if self.next_node != None:
			self.next_node.print_element()

	def delete(self,element):
		

if __name__ == '__main__':

	p = LinkedList()
	i = 0
	while i < 10:
		p.insert(i)
		i += 1
	p.print_elements()