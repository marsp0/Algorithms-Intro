package main

import (
	"fmt"
)

func main() {
	var graph = NewGraph(false)
	graph.AddVertex("A")
	graph.AddVertex("B")
	graph.AddVertex("C")
	graph.AddVertex("D")
	graph.AddEdge("A", "B")
	graph.AddEdge("B", "C")
	graph.AddEdge("B", "D")
	// graph.AddEdge("A", "D")
	// graph.RemoveEdge("B", "D")
	graph.RemoveVertex("B")

	graph.AddEdge("C", "D")
	graph.BreadthFirstSearch("A")
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
			for i := 0; i < len(graph.vertices[currentVertex].edges); i++ {
				// increments the distance of the node on the other side of the edge.
				if graph.vertices[currentVertex].edges[i].distance == 0 {
					graph.vertices[currentVertex].edges[i].distance = graph.vertices[currentVertex].distance + 1
					queue = append(queue, graph.vertices[currentVertex].edges[i].id)
				}
			}
		}
	}
}

// DepthFirstSearch - does a DFS on the graph and updates the distances of the visited nodes.
func (graph *Graph) DepthFirstSearch(id string) {
	// running time is the same as BFS - O(V + E)
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
			for i := 0; i < len(graph.vertices[currentVertex].edges); i++ {
				if graph.vertices[currentVertex].edges[i].state == 1 {
					fmt.Println("found a cycle")
				} else if graph.vertices[currentVertex].edges[i].state == 0 {
					stack = append(stack, graph.vertices[currentVertex].edges[i].id)
					enterExit = append(enterExit, false)
				}
			}
		}
	}
}

// AddVertex - adds a vertex with no edges to the graph.
func (graph *Graph) AddVertex(val string) {
	graph.vertices[val] = &Vertex{val, []*Vertex{}, 0, 0, 0}
}

// RemoveVertex - removes a vertex from the graph.
func (graph *Graph) RemoveVertex(val string) {

	for _, value := range graph.vertices {
		if value.id != val {
			for i := 0; i < len(value.edges); i++ {
				if value.edges[i].id == val {
					value.edges = append(value.edges[:i], value.edges[i+1:]...)
					break
				}
			}
		}
	}
	delete(graph.vertices, val)
}

// AddEdge - adds an edge to the graph
func (graph *Graph) AddEdge(val1, val2 string) {
	graph.vertices[val1].edges = append(graph.vertices[val1].edges, graph.vertices[val2])
	if !graph.directed {
		graph.vertices[val2].edges = append(graph.vertices[val2].edges, graph.vertices[val1])
	}
}

// RemoveEdge - removes an edge from the graph.
func (graph *Graph) RemoveEdge(val1, val2 string) {
	var toRemove int
	for i := 0; i < len(graph.vertices[val1].edges); i++ {
		if graph.vertices[val1].edges[i].id == val2 {
			toRemove = i
			break
		}
	}
	graph.vertices[val1].edges = append(graph.vertices[val1].edges[:toRemove], graph.vertices[val1].edges[toRemove+1:]...)
	if !graph.directed {
		for i := 0; i < len(graph.vertices[val2].edges); i++ {
			if graph.vertices[val2].edges[i].id == val1 {
				toRemove = i
				break
			}
		}
		graph.vertices[val2].edges = append(graph.vertices[val2].edges[:toRemove], graph.vertices[val2].edges[toRemove+1:]...)
	}
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
	id    string
	edges []*Vertex

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
