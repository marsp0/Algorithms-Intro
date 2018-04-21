package main

// TO BE FILLED

// RedBlackTree - balanced binary search tree
type RedBlackTree struct {
	root *RedBlackNode
}

// RedBlackNode - struct representing the node information + color
type RedBlackNode struct {
	Node
	red bool
}

type NILNode struct {
}
