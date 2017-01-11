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

if __name__ == '__main__':

	vertices = [1,2,3,4,5,6]
	edges = [(1,2),(1,4),(2,3),(2,4),(2,6),(1,5),(5,3)]
	stack = topological_sort(vertices,edges)
	print stack.traverse()
