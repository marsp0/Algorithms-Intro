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

'''