from queue import DoubleQueue as Queue
from stack import Stack

class Graph(object):

	def __init__(self):

		self._graph = {}
		self._size = 0
		self._degree = {}

	def add(self,vert_1, vert_2=None):
		vert_1 = vert_1.lower()
		if vert_2 != None:
			vert_2 = vert_2.lower()
			self._graph[vert_1].edges.append(vert_2)
			self._graph[vert_2].edges.append(vert_1)
			self._degree[vert_1] += 1
			self._degree[vert_2] += 1
		else:
			self._graph[vert_1] = Vertex(vert_1)
			self._size += 1
			self._degree[vert_1] = 1
		return True

	def remove(self,vert_1,vert_2=None):

		if vert_2 != None:
			self._graph[vert_1].edges.remove(vert_2)
			self._graph[vert_2].edges.remove(vert_1)
			self._degree[vert_1] -= 1
			self._degree[vert_2] -= 1
		else:
			del self._graph[vert_1]
			del self._degree[vert_1]
			self._size -= 1

	def breadth_first(self,root):
		#create the queue
		queue = Queue()
		for item in self._graph.values():
			item.distance = 0
		queue.enqueue(self._graph[root])
		while not (queue.is_empty()):
			current = queue.dequeue()
			for node in current.edges:
				#the iteration is over the edge list which is just strings
				#so we need the actual nodes.
				node = self._graph[node]
				if node.distance == 0:
					node.distance = current.distance + 1
					node.parent = current
					queue.enqueue(node)

	def depth_first(self, root):

		stack = Stack()
		pass


		

class Vertex(object):

	def __init__(self,name):
		self.name = name
		self.distance = 0
		self.parent = None
		self.edges = []

	def __repr__(self):
		return '{}'.format(str(self.name))


if __name__ == '__main__':
	graph = Graph()
	graph.add('A')
	
	graph.add('B')
	
	graph.add('C')
	graph.add('D')
	graph.add('a','b')
	graph.add('b','c')
	graph.add('c','d')
	graph.add('A','D')
	graph.breadth_first('b')
	for item in graph._graph.values():
		print item.name, item.parent
