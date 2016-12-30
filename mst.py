class WeightedGraph(object):

	def __init__(self, vertices, weights, edges):

		self.weights, self.edges = self.sort_edges(weights,edges)
		self.vertices = vertices

	def get_mst_kruskal(self):

		''' The idea is the following, we start iterating over the sorted edges and
			and if the edge is not in the temp list, then this means that we can add it,
			if it is, it means that it is a cycle and so we skip it.
		'''

		temp_edges = [self.edges.pop(0)]
		temp_vertices = [vertex for vertex in temp_edges[0]]
		for edge in self.edges:
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

	weights = [1,2,3,4,5,6,1]
	edges = [(1,2),(1,3),(3,6),(2,4),(2,6),(4,5),(2,3)]
	vertices = [1,2,3,4,5,6]

	p = WeightedGraph(vertices,weights,edges)
	print p.get_mst_kruskal()