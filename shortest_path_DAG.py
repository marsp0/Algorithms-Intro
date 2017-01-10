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