class NaivePriorityQ(object):

	def __init__(self):

		self.node = None
		self.min = None

	def insert(self,data, priority):

		if self.node == None:

			self.node = Node(data,priority)



class Node(object):

	def __init__(self,data=None,priority = 'low'):

		self.data = data
		self.priority = priority