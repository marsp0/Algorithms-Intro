package main

import (
	"fmt"
)

func main() {
	var graph = NewGraph(true)
	graph.AddVertex("A")
	graph.AddVertex("B")
	graph.AddVertex("C")
	graph.AddVertex("D")
	graph.AddEdge("A", "B")
	graph.AddEdge("B", "C")

	// graph.AddEdge("A", "D")
	graph.AddEdge("C", "D")
	graph.AddEdge("B", "D")
	graph.DepthFirstSearch("A")
	fmt.Println(graph.vertices["D"].distance)
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
	directed bool
}

// BreadthFirstSearch - does a BFS on the graph from the given node.
func (graph *Graph) BreadthFirstSearch(id string) {
	// Running time - O(V + E)
	graph.Reset()
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
	graph.Reset()
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
func (graph *Graph) IsAcyclic(id string) bool {
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
	graph.Reset()
	var (
		stack     = []string{id}
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
	return true
}

// AddVertex - adds a vertex with no edges to the graph.
func (graph *Graph) AddVertex(val string) {
	graph.vertices[val] = &Vertex{val, map[string]*Vertex{}, map[string]int{}, 0, 0, 0}
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
	delete(graph.vertices, val)
}

// AddEdge - adds an edge to the graph
func (graph *Graph) AddEdge(val1, val2 string) {
	graph.vertices[val1].edges[val2] = graph.vertices[val2]
	if !graph.directed {
		graph.vertices[val2].edges[val1] = graph.vertices[val1]
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
}

// BoruvkaMST - implements the algorithm from the wiki link. TO BE DONE
func (graph *Graph) BoruvkaMST() {
	// https://en.wikipedia.org/wiki/Bor%C5%AFvka%27s_algorithm
	return
}

// KruskalMST - https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
func (graph *Graph) KruskalMST() {
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

}

// Reset - function that resets all the modifiable attributes of a Node.
func (graph *Graph) Reset() {
	for _, value := range graph.vertices {
		value.distance = 0
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
	color    int
	distance int
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
