from linked_list import LinkedList



class HashTable(object):
	"""docstring for HashTable"""
	def __init__(self):
		super(HashTable, self).__init__()
		self.array = []

	def get_index(self,string):

		hashed = hash(string)
		index = hashed % len(self.array)
		return index

	def get (self,string):
		pass

	def add(self,key,data):

		pass