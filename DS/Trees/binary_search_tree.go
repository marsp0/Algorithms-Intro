package main

// Binary Search Tree property

// Let x be a node in a binary search tree. The left nodes contains keys that are less
// than or equal to the parent. The right child contains keys that are greater than or equal
// to the parent. Can be implemented using Linked Lists.
//
//
// Balanced BST - O(lgn) worst case running time for the usual operations.
// BST - O(n) worst case running time because the data structure could end up being
// a normal linked list.

// Inorder tree walk - prints left -> root -> right
// Preorder tree walk - prints root -> left -> right / root -> right -> left
// Postorder tree walk - prints left -> right -> root / right -> left -> root

func main() {

}

// BinarySearchTree - represents a BST
type BinarySearchTree struct {
	root *Node
}

// Search - returns a pointer to the required node
func (tree *BinarySearchTree) Search(node *Node, val int) *Node {
	if node != nil {
		if node.key == val {
			return node
		}
		if node.key > val {
			if node.left != nil {
				return tree.Search(node.left, val)
			}
		} else {
			if node.right != nil {
				return tree.Search(node.right, val)
			}
		}
	}
	return nil
}

// MinElement - returns the min element in the tree
func (tree *BinarySearchTree) MinElement(node *Node) *Node {
	for node.left != nil {
		node = node.left
	}
	return node
}

// MaxElement - returns the max element in the BST
func (tree *BinarySearchTree) MaxElement(node *Node) *Node {
	for node.right != nil {
		node = node.right
	}
	return node
}

// Successor - returns the successor of a node in the BST
func (tree *BinarySearchTree) Successor(node *Node) *Node {
	// if there is a right subtree, then we just find the min element in it.
	// Otherwise we search for the first node that has the current node in its left subtree.
	// This means that this would be the first node larger than the current one.
	if node.right != nil {
		return tree.MinElement(node.right)
	}
	var y = node.parent
	for node.parent != nil && node == y.right {
		node = y
		y = y.parent
	}
	return y
}

// Predecessor - returns the predecessor of the given node.
func (tree *BinarySearchTree) Predecessor(node *Node) *Node {
	// If there is a left subtree, then we just get the max element in it.
	// if there isnt a left subtree, then we look for the first node (from our current node upwards) that
	// that has our current mode in its right subtree. This means that the current node is the first
	// node larger than it.
	// 					+-------+
	// 					|    8	|
	// 					|    	|
	//			 		+-------+
	//			 		|	^	|
	//			 		|	|p	|
	//			 +-------+	|r	+-------+
	//			 |   4 	 |	|e	|   16 	|
	//			 |    	 |	|d	|    	|
	//			 +-------+	|e	+-------+
	//			 			|s	|		|
	//			 			|	|		|
	//			 		+-------+		+-------+
	//			 		|   12 	|		|   17 	|
	//			 		|    	|		|    	|
	//			 		+-------+		+-------+
	//			 				|
	//			 				|
	//			 				+-------+
	//			 				|   14 	|
	//			 				|    	|
	//			 				+-------+

	if node.left != nil {
		return tree.MaxElement(node.left)
	}
	var y = node.parent
	for node.parent != nil && node == y.left {
		node = y
		y = y.parent
	}
	return y
}

// Node - represents a node in the tree
type Node struct {
	parent *Node
	key    int
	data   int
	left   *Node
	right  *Node
}
