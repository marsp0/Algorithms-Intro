'''	Bellman-Ford's Algorithm for shortest paths.

	The algorithm uses the notion of Relaxation and Initialization.

	Initialization: 

	1. iterate over the vertices and set the current minimum weight needed to get to that vertex
	to infinity. Set the predecessor to nil
	2. set the current min weight of the source to 0 because we start at it

	Relaxation(u,v,w) :

	if v.d > u.d + w(u,v):
		v.d = u.d + w(u,v)
		v.pi = u

	PSEUDOCODE

	1. Initialize the algorithm
	2. for i = 1 to len(G.V)
	3.     for (u,v) in G.E
	4.         Relax(u,v,w)
	   #at this point we should have the min weights on each edge
	5. for (u,v) in G.E
	6.     if v.d > u.d + w(u,v)
	7.         return False
	8. return True

	Complexity :

	O(T) = O(V + VE + E) #initialization takes V, line 2-4 takes VE , line 5-8 takes E
	     = O(VE)
	     = O(V^3)  #E = O(V^2)

'''

import sys

vert_structure = {}

def bellman_ford(vertices, edges, source):
	#initialization
	for vertex in vertices:
		vert = Vertex(vertex)
		vert_structure[vertex] = vert
	vert_structure[source].current_min_weight = 0
	#build the actual shortest path
	for i in xrange(len(vertices) - 1):
		for edge in edges:
			relax(edge)
	#check for cycles
	for edge in edges:
		first = edge[0]
		second = edge[1]
		weight = edge[2]
		if vert_structure[second].current_min_weight > vert_structure[first].current_min_weight + weight:
			return False
	return True

def relax(edge):
	first = edge[0]
	second = edge[1]
	weight = edge[2]
	if vert_structure[second].current_min_weight > vert_structure[first].current_min_weight + weight:
		vert_structure[second].current_min_weight = vert_structure[first].current_min_weight + weight
		vert_structure[second].predecessor = vert_structure[first].name

class Vertex(object):

	def __init__(self,name):

		self.name = name
		self.current_min_weight = sys.maxsize
		self.predecessor = None

if __name__ == '__main__':

	vertices = [1,2,3,4,5,6]
	edges = [(1,2,5), (1,3,3), (2,3,1), (1,4,2), (1,6,1), (2,5,4), (4,5,6)]
	bellman_ford(vertices,edges,2)
	for vert in vert_structure.values():
		print vert.name
		print vert.current_min_weight
		print vert.predecessor
		print
		print