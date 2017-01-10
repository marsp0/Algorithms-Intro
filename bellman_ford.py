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