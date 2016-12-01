''' Queue Data structure using a doubly linked list and a singly linked list'''


class DoubleQueue(object):

	def __init__(self, data = None):

		self.head = None
		self.tail = None
		self._len = 0


	def enqueue(self,data):

		if self.head == None:
			self.head = Node(data)
		else:
			if self.tail == None:
				self.tail = Node(data)
				self.head.next, self.tail.prev = self.tail, self.head
			else:
				new_node = Node(data)
				new_node.prev, self.tail.next = self.tail, new_node
				self.tail = new_node
		self._len += 1

	def dequeue(self):
		if self.head != None:
			to_return = self.head
			self.head = to_return.next
			self._len -= 1
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
	p.enqueue(3)
	print p.dequeue()
	print p.dequeue()
	print p.dequeue()
	print p.dequeue()
	