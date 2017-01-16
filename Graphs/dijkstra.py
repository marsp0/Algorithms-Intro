''' Dijkstra's algorithm - faster than Bellman Ford if the weights are non negative
	
	Uses the notion of relaxation and initialization

	initialization

	1. set every vertex' predesessor to NIL
	2. set evert vertex' current min weight to ifininty
	3. additional implementation helpers are set during this phase

	Relaxation(u,v,w) :

	if v.d > u.d + w(u,v):
		v.d = u.d + w(u,v)
		v.pi = u

	PSEUDOCODE

	1. Initialization
	2. Build the PQ and the empty processed vertices set S
	3. While PQ:
	4.     u = Extract-Min(PQ)
	5.     S = S + {u}
	6.     for edge in adjacency vertices of u
	7.         relax(u,edge,w)

	Complexity:



'''

from bellman_ford import Vertex
import sys

def dijkstra(vertices,edges,root):
	#initialization
	graph = {}
	index_map = {}
	for vertex in vertices:
		graph[vertex] = Vertex_1(vertex)
	for edge in edges:
		graph[edge[0]].edges.append((edge[1],edge[2]))
	heap = [[v,sys.maxsize] for v in vertices]
	heap = build(heap,index_map)
	heap[index_map[root]][1] = 0
	graph[root].current_min_weight = 0
	for item in xrange(len(heap)):
		index_map[heap[item][0]] = item
	while heap:
		current = extract(heap,index_map)
		node_name = current[0]
		node_weight = current[1]
		for edge in graph[node_name].edges:
			edge_name = edge[0]
			edge_weight = edge[1]
			if graph[edge_name].current_min_weight > graph[node_name].current_min_weight + edge_weight:
				graph[edge_name].current_min_weight = graph[node_name].current_min_weight + edge_weight
				graph[edge_name].predecessor = node_name
				heap[index_map[edge_name]][1] =  graph[node_name].current_min_weight + edge_weight
				bubble_up(heap,index_map[edge_name],index_map)
	return graph

class Vertex_1(Vertex):

	def __init__(self,name):
		super(Vertex_1,self).__init__(name)
		self.edges = []


##############################################
#		copied from the heap.py
#		modified to use the heap structure with dijkstra
##############################################
		
def bubble_down(array,index,index_map):
	size = len(array)
	while (index*2 + 2) <= size:
		min_index = min_child(array,index)
		index_map[array[min_index][0]] = min_index
		if min_index != False:
			array[index], array[min_index] = array[min_index], array[index]
			index = min_index
		else:
			break
	return True

def min_child(array,index):
	size = len(array)
	if (index*2 + 2) < size:
		if array[index*2 + 1][1] < array[index][1] or array[index*2 + 2][1] < array[index][1]:
			if array[index*2 + 1][1] < array[index*2 + 2][1]:
				return (index*2 + 1)
			else:
				return (index*2 + 2)
	else:
		if array[index*2 + 1][1] < array[index][1]:
			return (index*2 + 1)
	return False


def build(array,index_map):
	size = len(array)
	for i in xrange((size)//2, -1,-1):
		bubble_down(array, i,index_map)
	return array

def extract(array,index_map):
	if len(array) == 1:
		return	array.pop()
	else:
		to_return = array[0]
		array[0] = array.pop(-1)
		bubble_down(array,0,index_map)
	return to_return

def insert(array,element,index_map):

	array.append(element)
	bubble_up(array, len(array)-1,index_map)
	return True

def bubble_up(array,index,index_map):
	while (index - 1)// 2 >= 0:
		if array[index][1] < array[(index - 1)//2][1]:
			array[index], array[(index - 1)//2] = array[(index - 1)//2], array[index]
		index = (index - 1) // 2
	index_map[array[index][0]] = index
	return True

if __name__ == '__main__':
	vertices = [1,2,3,4,5,6]
	edges = [(1,2,1),(1,4,2),(2,3,1),(2,4,4),(2,6,2),(1,5,3),(5,3,1)]
	graph = dijkstra(vertices,edges,1)
	for item in graph.values():
		print item.name, 'name'
		print item.current_min_weight
		print item.predecessor ,'predecessor'
		print item.edges
		print
		print