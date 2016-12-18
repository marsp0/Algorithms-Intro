class Graph(object):

	def __init__(self):

		self._graph = {}
		self._size = 0
		self._degree = {}

	def add(self,vert_1, vert_2=None):

		if vert_2 != None
			self._graph[vert_1].append(vert_2)
			self._degree[vert_1] += 1
		else:
			self._graph[vert_1] = []
			self._size += 1
			self._degree[vert_1] = 1
		return True

	def remove(self,vert_1,vert_2=None):

		if vert_2 != None:
			self._graph[vert_1].remove(vert_2)
			self._degree[vert_1] -= 1
		else:
			del self._graph[vert_1]
			del self._degree[vert_1]
			self._size -= 1

	def breadth_first(self):

		pass