''' Queue Data structure using a doubly linked list and a singly linked list'''


class DoubleQueue(object):

	def __init__(self, data = None):

		self.head = None
		self.tail = None
		self._len = 0


	def enqueue(self,data):

		if self.head == None:
			print 'was once here'
			self.head = self.tail = Node(data)
		else:
			new_node = Node(data)
			new_node.prev = self.tail
			self.tail = new_node

	def dequeue(self):
		if self.head != None:
			to_return = self.head
			self.head = to_return.next
			return to_return.data
		else:
			return False


	def __len__(self):

		return self._len



class Node(object):

	def __init__(self, data = None):

		self.prev = None
		self.data = data
		self.next = None


if __name__ == '__main__':

	p = DoubleQueue()
	p.enqueue(1)
	p.enqueue(2)
	p.enqueue(3)
	print p.dequeue()
	print p.dequeue()
	print p.dequeue()
	print p.dequeue()