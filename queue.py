''' Queue Data structure using a doubly linked list and a singly linked list'''


class DoubleQueue(object):

	'''
		Insertion and deletion in this implementation are O(1)

	'''

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

class SingleQueue(object):
	''' implementing it with signly linked list logic.

		insertion here is O(n)
		deleteion is O(1) 

	'''

	def __init__(self):

		self.head = SingleNode()
		self._len = 0

	def enqueue(self,data):

		self.head.insert(data)
		self._len += 1

	def dequeue(self):
		to_return = self.head
		self.head = to_return.next
		self._len -= 1
		return to_return.data

	def __len__(self):

		return self._len

class SingleNode(object):

	def __init__(self,data = None):
		self.data = data
		self.next = None

	def insert(self,data):
		if self.data == None:
			self.data = data
			self.next = SingleNode()
		else:
			self.next.insert(data)

class Node(object):

	def __init__(self, data = None):

		self.prev = None
		self.data = data
		self.next = None

