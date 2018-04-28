package main

import (
	"fmt"
	"math"
)

func main() {
	var graph = NewGraph(true)
	graph.AddVertex("undershorts")
	graph.AddVertex("socks")
	graph.AddVertex("watch")
	graph.AddVertex("pants")
	graph.AddVertex("shoes")
	graph.AddVertex("shirt")
	graph.AddVertex("belt")
	graph.AddVertex("tie")
	graph.AddVertex("jacket")
	graph.AddEdge("undershorts", "pants", 1)
	graph.AddEdge("undershorts", "shoes", 1)
	graph.AddEdge("socks", "shoes", 1)
	graph.AddEdge("pants", "belt", 1)
	graph.AddEdge("shirt", "belt", 1)
	graph.AddEdge("shirt", "tie", 1)
	graph.AddEdge("belt", "jacket", 1)
	graph.AddEdge("tie", "jacket", 1)
	graph.AddEdge("pants", "shoes", 1)
	fmt.Println(graph.TopologicalSort("undershorts"))
}

// NewGraph - returns a new graph object
func NewGraph(directed bool) *Graph {
	var graph = &Graph{}
	var verts = make(map[string]*Vertex)
	graph.vertices = verts
	graph.directed = directed
	return graph
}

// Graph struct represents a graph object
type Graph struct {
	vertices map[string]*Vertex
	edges    [][2]string
	directed bool
}

// BreadthFirstSearch - does a BFS on the graph from the given node.
func (graph *Graph) BreadthFirstSearch(id string) {
	// Running time - O(V + E)
	graph.Reset(false)
	var queue = []string{id}
	// We iterate as long as the Q is not empty
	for len(queue) > 0 {
		// Using a slice instead of a Q
		// Not sure about the
		// According to a user from https://www.reddit.com/r/golang/comments/8e492w/running_time_of_the_slicing_operation/
		// The "queue = queue[1:]" runs in O(1)
		var currentVertex = queue[0]
		queue = queue[1:]
		// If the vertex has not been visited, we
		// mark it as visited (state = 2) and
		// add its edges to the queue.
		// We also increase the distance from the root to it.
		if graph.vertices[currentVertex].state == 0 {
			graph.vertices[currentVertex].state = 2
			for key, value := range graph.vertices[currentVertex].edges {
				if value.distance == 0 {
					value.distance = graph.vertices[currentVertex].distance + 1
					queue = append(queue, key)
				}
			}
		}
	}
}

// DepthFirstSearch - does a DFS on the graph and updates the distances of the visited nodes.
func (graph *Graph) DepthFirstSearch(id string) {
	// running time is the same as BFS - O(V + E)
	graph.Reset(false)
	var (
		stack = []string{id}
	)
	for len(stack) > 0 {
		var (
			currentVertex = stack[len(stack)-1]
		)
		stack = stack[:len(stack)-1]
		if graph.vertices[currentVertex].state == 0 {
			for key := range graph.vertices[currentVertex].edges {
				stack = append(stack, key)
			}
		}

	}
}

// IsAcyclic - shows if the graph contains cycles or not.
func (graph *Graph) IsAcyclic() bool {
	// Types of edges
	// 1. Tree edges - regular
	// 2. back edge - edge (u,v) is a back edge if it connects u to an ancestor v
	// in a depth first tree. This means that there is a cycle.
	// 3. Forward edges - an edge that connects two already discovered vertices.
	// 4. Cross edges - all other edges.

	// Cycle detection
	//  UNDIRECTED GRAPH
	// 	- no difference between cross/forward/back edge. Cycles are easier to detect.
	// 	We just keep track of what we have detected so far and if we see an already detected node,
	// 	then we have a cycle.
	//
	// 	DIRECTED GRAPH
	// 	- Harder to detect, but thanks to (https://stackoverflow.com/questions/46506077/how-to-detect-cycles-in-a-directed-graph-using-the-iterative-version-of-dfs)
	//  not impossible. I was aware of the recursive way, but was not sure of how to achieve it iteratively.
	graph.Reset(false)
	for key, value := range graph.vertices {
		fmt.Println(key, value.state)
		if value.state != 2 {
			var (
				stack     = []string{key}
				enterExit = []bool{false}
			)
			for len(stack) > 0 {
				var (
					currentVertex = stack[len(stack)-1]
					action        = enterExit[len(enterExit)-1]
				)
				stack = stack[:len(stack)-1]
				enterExit = enterExit[:len(enterExit)-1]
				if action {
					// node is exiting
					graph.vertices[currentVertex].state = 2
				} else {
					graph.vertices[currentVertex].state = 1
					stack = append(stack, currentVertex)
					enterExit = append(enterExit, true)
					// iterate over the edges of the graph.
					for key, value := range graph.vertices[currentVertex].edges {
						if value.state == 1 {
							return false
						} else if value.state == 0 {
							stack = append(stack, key)
							enterExit = append(enterExit, false)
						}
					}
				}
			}
		}
	}
	return true
}

// TopologicalSort - sorts the elements in a DAG
func (graph *Graph) TopologicalSort(val string) []string {
	var result = []string{}
	graph.Reset(false)
	for key, value := range graph.vertices {
		if value.state != 2 {
			graph.topologicalVisit(key, &result)
		}
	}
	return result
}

func (graph *Graph) topologicalVisit(val string, result *[]string) {
	graph.vertices[val].state = 1
	for key, value := range graph.vertices[val].edges {
		if value.state == 0 {
			graph.topologicalVisit(key, result)
		}
	}
	graph.vertices[val].state = 2
	*result = append(*result, val)
}

// AddVertex - adds a vertex with no edges to the graph.
func (graph *Graph) AddVertex(val string) {
	graph.vertices[val] = &Vertex{val, map[string]*Vertex{}, map[string]int{}, 0, 0, 0, nil}
}

// RemoveVertex - removes a vertex from the graph.
func (graph *Graph) RemoveVertex(val string) {
	if graph.directed {
		for _, value := range graph.vertices {
			if value.id != val {
				delete(value.edges, val)
				delete(value.weights, val)
			}
		}
	} else {
		for key := range graph.vertices[val].edges {
			delete(graph.vertices[key].edges, val)
			delete(graph.vertices[key].weights, val)
		}
	}
	for index, value := range graph.edges {
		if value[0] == val || value[1] == val {
			graph.edges = append(graph.edges[:index], graph.edges[index+1:]...)
		}
	}
	delete(graph.vertices, val)
}

// AddEdge - adds an edge to the graph
func (graph *Graph) AddEdge(val1, val2 string, weight int) {
	graph.vertices[val1].edges[val2] = graph.vertices[val2]
	graph.edges = append(graph.edges, [2]string{val1, val2})
	graph.vertices[val1].weights[val2] = weight
	if !graph.directed {
		graph.vertices[val2].edges[val1] = graph.vertices[val1]
		graph.edges = append(graph.edges, [2]string{val2, val1})
		graph.vertices[val2].weights[val1] = weight
	}
}

// RemoveEdge - removes an edge from the graph.
func (graph *Graph) RemoveEdge(val1, val2 string) {
	delete(graph.vertices[val1].edges, val2)
	delete(graph.vertices[val1].weights, val2)
	if !graph.directed {
		delete(graph.vertices[val2].edges, val1)
		delete(graph.vertices[val2].weights, val1)
	}
	for index, tuple := range graph.edges {
		if tuple[0] == val1 && tuple[1] == val2 || tuple[0] == val2 && tuple[1] == val1 {
			graph.edges = append(graph.edges[:index], graph.edges[index+1:]...)
		}
	}
}

// BoruvkaMST - implements the algorithm from the wiki link. TO BE DONE
func (graph *Graph) BoruvkaMST() {
	// https://en.wikipedia.org/wiki/Bor%C5%AFvka%27s_algorithm
	return

}

// BellmanFord - returns the shortest path from source to destination using
// Bellman-Ford's algorithm.
func (graph *Graph) BellmanFord(source string) bool {
	// Running time O(V * E)
	graph.Reset(true)
	graph.vertices[source].distance = 0
	for _, vertex := range graph.vertices {
		for _, edge := range graph.edges {
			graph.Relax(edge[0], edge[1], vertex.weights[edge[1]])
		}
	}
	for _, edge := range graph.edges {
		if graph.vertices[edge[1]].distance > graph.vertices[edge[0]].distance+graph.vertices[edge[0]].weights[edge[1]] {
			return false
		}
	}
	return true
}

// Relax - relaxes a vertex by checking if the current distance it has is smaller by the distance of the previous vertex + the weight.
func (graph *Graph) Relax(source, destination string, weight int) {
	if graph.vertices[destination].distance > graph.vertices[source].distance+weight {
		graph.vertices[destination].distance = graph.vertices[source].distance + weight
		graph.vertices[destination].predecessor = graph.vertices[source]
	}
}

// Reset - function that resets all the modifiable attributes of a Node.
func (graph *Graph) Reset(shortestPath bool) {
	for _, value := range graph.vertices {
		if shortestPath {
			value.distance = math.MaxInt32

		} else {
			value.distance = 0
		}
		value.predecessor = nil
		value.color = 0
		value.state = 0
	}
}

// Vertex - represents a vertex in the graph
type Vertex struct {
	id      string
	edges   map[string]*Vertex
	weights map[string]int
	// 0 - not processed
	// 1 - started processing
	// 2 - processed

	state int

	// 0 - white
	// 1 - grey
	// 2 - black
	color       int
	distance    int
	predecessor *Vertex
}

// KruskalMST - https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
func KruskalMST(vertices []string, edges [][2]string, weights []int) [][2]string {
	// we dont need state, distances etc so the graph representation as separate slices.

	// TODO : FIGURE OUT HOW WE WILL RETURN THE TREE.

	// Cut - partition of the vertices of a graph into two disjoint sets. Any cut determines a cut-set, the set
	// of edges that have one endpoint in each subset of the partition. These edges are said to cross the cut.

	// Greedy approach properties
	// 1. Optimal substructure - optimal solution to problem incorporates optimal solutions to subproblems.
	// 2. Greedy choice property - Locally optimal choices lead to globally optimal solution.

	// Optimal substructure for MST : if e = [u,v] in an edge of some MST

	// Pseudocode
	// A = nil
	// for each vertex v
	// 		make set(v)
	// sort edges in increasing order
	// for each edge (u,v)
	// if find-set(u) != find-set(v)
	// 		A = A + (u,v)
	// return A

	// Runtime
	//
	var result = [][2]string{}
	var unionfind = NewUnionFind()
	for _, vertex := range vertices {
		unionfind.MakeSet(vertex)
	}
	// sort the edges
	Quicksort(edges, weights, 0, len(edges)-1)
	for index := range weights {
		if unionfind.FindRoot(edges[index][0]) != unionfind.FindRoot(edges[index][1]) {
			result = append(result, edges[index])
			unionfind.Union(edges[index][0], edges[index][1])
		}
	}
	return result
}

// Quicksort - sorts the edges in Kruskal
func Quicksort(edges [][2]string, weights []int, first, last int) {
	if first < last {
		var pivot = Partition(edges, weights, first, last)
		Quicksort(edges, weights, first, pivot-1)
		Quicksort(edges, weights, pivot+1, last)

	}
}

// Partition - helper function for Quicksort
func Partition(edges [][2]string, weights []int, first, last int) int {
	var (
		pivotIndex = last
		pivot      = weights[pivotIndex]
		wall       = first - 1
		current    = first
	)
	for current < last {
		if weights[current] <= pivot {
			wall++
			weights[wall], weights[current] = weights[current], weights[wall]
			edges[wall], edges[current] = edges[current], edges[wall]
		}
		current++
	}
	weights[wall+1], weights[pivotIndex] = weights[pivotIndex], weights[wall+1]
	edges[wall+1], edges[pivotIndex] = edges[pivotIndex], edges[wall+1]
	return wall + 1
}

// UnionFind data structure for the Kruskal algorithm.
type UnionFind struct {
	elements map[string]string
	size     map[string]int
}

// NewUnionFind - returns a new UnionFind data structure
func NewUnionFind() *UnionFind {
	var ds = &UnionFind{}
	ds.elements = make(map[string]string)
	ds.size = make(map[string]int)
	return ds
}

// MakeSet - makes a set for the given string
func (unionfind *UnionFind) MakeSet(id string) {
	unionfind.elements[id] = id
	unionfind.size[id] = 1
}

// FindRoot - finds the root of the given element.
func (unionfind *UnionFind) FindRoot(id string) string {
	for unionfind.elements[id] != id {
		id = unionfind.elements[id]
	}
	return id
}

// Union - performs union on the given values.
func (unionfind *UnionFind) Union(val1, val2 string) {
	var (
		root1 = unionfind.FindRoot(val1)
		root2 = unionfind.FindRoot(val2)
	)
	if unionfind.size[root1] < unionfind.size[root2] {
		unionfind.elements[root1] = root2
		unionfind.size[root2] += unionfind.size[root1]
		delete(unionfind.size, root1)
	} else {
		unionfind.elements[root2] = root1
		unionfind.size[root1] += unionfind.size[root2]
		delete(unionfind.size, root2)

	}
}
