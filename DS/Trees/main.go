package main

func main() {
	// var s = BinarySearchTree{nil}
	// var arr = []int{5, 6, 2, 8, 3, 10, 7, 11, 9}
	// for i := 0; i < len(arr); i++ {
	// 	var p = &Node{
	// 		parent: nil,
	// 		key:    arr[i],
	// 		data:   i,
	// 		left:   nil,
	// 		right:  nil,
	// 	}
	// 	s.Insert(p)
	// }
	// var x = s.Search(s.root, 8)
	// s.Delete(x)
	// s.InOrderTraversal()

	var p = RedBlackTree{nil}
	p.root = &RedBlackNode{
		Node: Node{
			parent: nil,
			key:    1,
			data:   1,
			left:   nil,
			right:  nil,
		},
		red: false,
	}
}
