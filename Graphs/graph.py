from queue import DoubleQueue as Queue
from stack import Stack

class Graph(object):

	def __init__(self, directed = False):

		self._graph = {}
		self._size = 0
		self._degree = {}
		self._directed = directed
		self.time = 0

	def add(self,vert_1, vert_2=None):
		vert_1 = vert_1.lower()
		if vert_2 != None:
			vert_2 = vert_2.lower()
			if not (vert_2 in self._graph[vert_1].edges) :
				self._graph[vert_1].edges.append(vert_2)
				if not self.is_directed():
					self._graph[vert_2].edges.append(vert_1)
					self._degree[vert_2] += 1
				self._degree[vert_1] += 1
		else:
			self._graph[vert_1] = Vertex(vert_1)
			self._size += 1
			self._degree[vert_1] = 1
		return True

	def remove(self,vert_1,vert_2=None):
		vert_1 = vert_1.lower()
		if vert_2 != None:
			vert_2 = vert_2.lower()
			if not self.is_directed():
				self._graph[vert_2].edges.remove(vert_1)
				self._degree[vert_2] -= 1
			self._graph[vert_1].edges.remove(vert_2)
			self._degree[vert_1] -= 1
		else:
			del self._graph[vert_1]
			del self._degree[vert_1]
		self._size -= 1

	def is_directed(self):
		return self._directed

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
					queue.enqueue(node)

	def depth_first(self, root):
		'''
			A search algorithm that goes as deep as it can in every subtree before
			backtrackingl.

			O(n) = |v + E| 

			Types of edges :
			1. Tree
			2. Back 
			3. Forward
			4. Cross

		'''
		stack = Stack()
		for item in self._graph.values():
			item.state = None
		stack.push(root)
		counter = 0
		while not (stack.is_empty()):
			node = self._graph[stack.pop()]
			if node.state == None:
				node.state = 'discovered + {}'.format(counter)
				for item in node.edges:
					stack.push(item)
				counter += 1

	#
	#Acyclic functions
	#
	
	def is_acyclic(self):
		for node in self._graph.keys():
			acyclic = self.is_acyclic_util(node)
			if acyclic == True:
				return True
		return False

	def is_acyclic_util(self, root):
		self._graph[root].start_processing = self.time
		self.time += 1
		self._graph[root].state = 'discovered'
		for node in self._graph[root].edges:
			if self._graph[node].state == None:
				self.is_acyclic_util(node)
		self._graph[root].end_processing = self.time
		self.time += 1

		for node in self._graph:
			for item in self._graph[node].edges:
				if self._graph[node].start_processing > self._graph[item].start_processing and self._graph[item].end_processing > self._graph[node].end_processing:
					return True
		return False

	#
	#Topological sorting functions
	#

	def topological_sort(self):
		#we cannot topologicaly sort a graph if it is not a DAG
		if not self.is_acyclic(): 
			visited = {}
			for i in self._graph:
				visited[i] = False
			stack = Stack()
			for node in self._graph:
				if visited[node] == False:
					self.topological_sort_util(node,visited,stack)
			return stack
		else:
			return False

	def topological_sort_util(self,node,visited,stack):

		'''node -  would be the node to get processed
			visited - the list where we append True if we have visited a node
			stack - the final list that we print in sorted order
		'''

		visited[node] = True
		for item in self._graph[node].edges:
			if visited[item] == False:
				self.topological_sort_util(item,visited,stack)
		stack.push(node)

	#
	#Prim's Algorithm
	#

	def get_prims_mst(self):

		'''using Prim's algorithm to obtain a minimum spaning tree '''

		if self.is_directed():
			
			

		else:
			return False

class Vertex(object):

	def __init__(self,name):
		self.name = name
		#BFS
		self.distance = 0
		#DFS
		self.state = None
		self.start_processing = 0
		self.end_processing = 0

		self.edges = []

	def __repr__(self):
		return '{}'.format(str(self.name))


if __name__ == '__main__':
	graph = Graph(True)
	graph.add('A')
	graph.add('B')
	graph.add('C')
	graph.add('D')
	graph.add('e')
	graph.add('f')
	graph.add('a','b')
	#graph.add('d','a')
	graph.add('b','e')
	graph.add('e','c')
	graph.add('c','f')
	graph.add('e','d')
	#graph.add('d','b')
	print graph.is_acyclic()