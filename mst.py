import sys

class WeightedGraph(object):

	def __init__(self, vertices, weights, edges):

		self.vertices = vertices
		self.weights = weights
		self.edges = edges

	def get_mst_kruskal(self):

		''' The idea is the following, we start iterating over the sorted edges and
			and if the edge is not in the temp list, then this means that we can add it,
			if it is, it means that it is a cycle and so we skip it.
		'''

		self.weights, self.edges = self.sort_edges(weights,edges)

		temp_edges = [self.edges.pop(0)]
		temp_vertices = [vertex for vertex in temp_edges[0]] #we add the first edge in order to have some base
		#iterate over the rest
		for edge in self.edges:
			#instead of making find-set function we can just do it here
			#if the two are different, then it means, that one of the vertices is not
			#in the list and so we just add it
			#if they are both present, then we just skip to avoid cycles
			first = edge[0] in temp_vertices
			second = edge[1] in temp_vertices
			if not ( first and second):
				temp_edges.append(edge)
				if not first:
					temp_vertices.append(edge[0])
				else:
					temp_vertices.append(edge[1])
		return temp_edges

	def sort_edges(self,weights,edges):

		#the lists for the weights division
		less_than = []
		greater_than = []
		pivot_list = []
		#the lists for the edges
		less_than_edges = []
		greater_than_edges = []
		pivot_edges = []

		#NOTE : is it possible to make it in place ?
		# is the place taken too much ?

		if len(weights) < 1:
			return weights,edges
		else:
			pivot_element = weights[0]

			for index in xrange(len(weights)):

				if weights[index] < pivot_element:

					less_than.append(weights[index])
					less_than_edges.append(edges[index])
				
				elif weights[index] > pivot_element:
				
					greater_than.append(weights[index])
					greater_than_edges.append(edges[index])

				else:

					pivot_list.append(weights[index])
					pivot_edges.append(edges[index])

			less_than, less_than_edges = self.sort_edges(less_than, less_than_edges)
			greater_than, greater_than_edges = self.sort_edges(greater_than,greater_than_edges)
		return (less_than + pivot_list + greater_than, less_than_edges + pivot_edges + greater_than_edges)

	def get_mst_prim(self):
		#NOTE : sadly i use two structures in order to be able to search in O(1)
		#NOTE : Is it possible to reduce that to 1 structure ?
		#NOTE : is adjacency matric better here ? 
		graph = self.create_vertices()
		graph_heap = build(graph)
		while len(graph_heap) != 0:
			print len(graph_heap)
			root = extract(graph_heap)
			for edge in root.edges:
				print edge

	def create_vertices(self):
		to_return = []
		for vertex in self.vertices:
			edge_list = []
			min_weight = sys.maxsize
			for index in xrange(len(self.edges)):
				if vertex in self.edges[index]:
					if self.edges[index][0] == vertex:
						edge_list.append((self.edges[index][1],self.weights[index]))
					else:
						edge_list.append((self.edges[index][0],self.weights[index]))
			vert = Vertex(vertex,edge_list,min_weight)	
			to_return.append(vert)
		return to_return			


class Vertex(object):

	def __init__(self,name,edges,min_weight):

		self.name = name
		self.edges = edges
		self.min_weight = min_weight

##############################################
#		copied from the heap.py
#		modified to use the heap structure
#		with VertexObject
##############################################
		
def bubble_down(array,index):
	size = len(array)
	while (index*2 + 2) <= size:
		min_index = min_child(array,index)
		if min_index != False:
			array[index], array[min_index] = array[min_index], array[index]
			index = min_index
		else:
			break
	return True

def min_child(array,index):
	size = len(array)
	if (index*2 + 2) < size:
		if array[index*2 + 1].min_weight < array[index].min_weight or array[index*2 + 2].min_weight < array[index].min_weight:
			if array[index*2 + 1].min_weight < array[index*2 + 2].min_weight:
				return (index*2 + 1)
			else:
				return (index*2 + 2)
	else:
		if array[index*2 + 1].min_weight < array[index].min_weight:
			return (index*2 + 1)
	return False


def build(array):
	size = len(array)
	for i in xrange((size)//2, -1,-1):
		bubble_down(array, i)
	return array

def extract(array):
	if len(array) == 1:
		return	array.pop()
	else:
		to_return = array[0]
		array[0] = array.pop(-1)
		bubble_down(array,0)
	return to_return


if __name__ == '__main__':

	weights = [1,2,3,4,5,6,1]
	edges = [(1,2),(1,3),(3,6),(2,4),(2,6),(4,5),(2,3)]
	vertices = [1,2,3,4,5,6]

	p = WeightedGraph(vertices,weights,edges)
	print p.get_mst_prim()