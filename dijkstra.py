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