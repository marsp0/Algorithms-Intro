''' Single source shortest path on DAG
	
	PSEUDOCODE:

	1. Topologically sort the vertices
	2. Initialization
	3. for u in the sorted array
	4.     for edge in ADJ[u]
	5.         Relax(u,edge,w)

	Complexity : 

	O(V+E) because we use DFS 

'''

from collections import defaultdict
from stack import Stack
from bellman_ford import Vertex


def topological_sort(vertices,edges):
	graph = {}
	visited = {}
	stack = Stack()
	for node in vertices:
		graph[node] = []
		visited[node] = False
	for edge in edges:
		graph[edge[0]].append(edge[1])
	for root in graph:
		if visited[root] == False:
			topological_util(root,graph,visited,stack)
	return stack


def topological_util(node,graph,visited,stack):

	visited[node] = True
	for edge in graph[node]:
		if visited[edge] == False:
			topological_util(edge,graph,visited,stack)
	stack.push(node)

def SSSP_DAG(vertices,edges,root):
	#sort the graph topologically
	stack = topological_sort(vertices,edges).traverse()
	#initialization
	graph = {}
	for node in vertices:
		graph[node] = Vertex_1(node)
		for edge in edges:
			if edge[0] == node:
				graph[node].edges.append((edge[1],edge[2]))

	#NOTE : is there an easier way to get that root value to be 0 ?
	for item in stack:
		if item == root:
			graph[root].current_min_weight = 0
	for item in stack:
		for edge in graph[item].edges:
			if graph[edge[0]].current_min_weight > graph[item].current_min_weight + edge[1]:
				graph[edge[0]].current_min_weight = graph[item].current_min_weight + edge[1]
				graph[edge[0]].predecessor = item
	return graph

class Vertex_1(Vertex):

	def __init__(self,name):
		super(Vertex_1,self).__init__(name)
		self.edges = []


if __name__ == '__main__':

	vertices = [1,2,3,4,5,6]
	edges = [(1,2,1),(1,4,2),(2,3,4),(2,4,4),(2,6,2),(1,5,3),(5,3,1)]
	graph = SSSP_DAG(vertices,edges,1)
	for item in graph.values():
		print item.name
		print item.current_min_weight
		print item.predecessor
		print item.edges
		print
