class WeightedGraph(object):

	def __init__(self, vertices, edges, weights):

		self.edges = edges
		self.weights = weights
		self.vertices = vertices
	
	def get_mst_kruskal(self):

		''' The idea is the following, we start iterating over the sorted edges and
			and if the edge is not in the temp list, then this means that we can add it,
			if it is, it means that it is a cycle and so we skip it.
		'''

	def sort_edges(self,weights,edges):

		#the lists for the weights division
		less_than = []
		greater_than = []
		pivot_list = []
		#the lists for the edges
		less_than_edges = []
		greater_than_edges = []
		pivot_edges = []

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

if __name__ == '__main__':

	p = WeightedGraph([1,2,3,4,5,6],[(1,2),(1,3),(2,4), (3,6),(5,6),(1,5)], [1,3,2,12,3,7])
	print p.sort_edges([1,3,2,12,3,7] , [(1,2),(1,3),(2,4), (3,6),(5,6),(1,5)] )