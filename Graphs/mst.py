import sys
from collections import defaultdict

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
		#
		# Thank God for this article : https://programmingpraxis.com/2010/04/09/minimum-spanning-tree-prims-algorithm/
		#
		#build the dict
		graph_dict = defaultdict(list)
		for index in xrange(len(self.edges)):
			first, second = self.edges[index]
			weight = self.weights[index]
			graph_dict[first].append((first,second,weight))
			graph_dict[second].append((second,first,weight))
		mst = []
		used = set([self.vertices[0]])
		usable = graph_dict[self.vertices[0]]
		usable = build(usable)
		while usable:
			first, second, weight = extract(usable)
			#first one is the one being checked
			if second not in used:
				used.add(second)
				mst.append((first,second,weight))
				for edge in graph_dict[second]:
					if edge[1] not in used:
						insert(usable,edge)
			print usable
		return mst

class Vertex(object):

	def __init__(self,name,edges):

		self.name = name
		self.edges = edges


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
		if array[index*2 + 1][2] < array[index][2] or array[index*2 + 2][2] < array[index][2]:
			if array[index*2 + 1][2] < array[index*2 + 2][2]:
				return (index*2 + 1)
			else:
				return (index*2 + 2)
	else:
		if array[index*2 + 1][2] < array[index][2]:
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

def insert(array,element):

	array.append(element)
	bubble_up(array, len(array)-1)
	return True

def bubble_up(array,index):
	while (index - 1)// 2 >= 0:
		if array[index][2] < array[(index - 1)//2][2]:
			array[index], array[(index - 1)//2] = array[(index - 1)//2], array[index]
		index = (index - 1) // 2
	return True


if __name__ == '__main__':

	weights = [1,2,3,4,5,6,1]
	edges = [(1,6),(1,4),(3,1),(2,5),(2,1),(4,5),(2,3)]
	vertices = [1,2,3,4,5,6]

	p = WeightedGraph(vertices,weights,edges)
	print p.get_mst_prim()