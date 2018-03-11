// Definition - priority queue is a datastructure for maintaining a set S of elements, each with an associated value called a key.
// A max-priority queue supports the following operations
// INSERT - inserts an element x into the set S which is equivalent to the operation S = S union {x}
// Max(S) - returns the element of S with the largest key
// Extract-Max(S) removes and returns the element of S with the largest Key
// Increase-Key(S, x, k) - increases the value of element x's key to the new value k, which is assumed to be at least as large as x's
// current key value.

package main

func main() {

}

// Item - represents an object in the PQ
type Item struct {
	key   int
	value int
}

// PQueue - holds the different items of the queue
type PQueue []*Item

// Len - returns the length of the q
func (pq PQueue) Len() int {
	return len(pq)
}

// Max - returns the first (also max) element of the Q
func (pq PQueue) Max() *Item {
	return pq[0]
}

// ExtractMax - extracts the max element of the PQ and heapifies the rest of the elements.
func (pq *PQueue) ExtractMax() *Item {
	var max = (*pq)[0]
	(*pq)[0] = (*pq)[pq.Len()-1]
	(*pq) = (*pq)[:pq.Len()-1]
	MaxHeapify(*pq, 0, pq.Len())
	return max
}

// Left -  returns the position of the left child
func Left(i int) int {
	return 2*i + 1
}

// Right - returns the position of the right child
func Right(i int) int {
	return 2*i + 2
}

// Parent - returns the position of the parent
func Parent(i int) int {
	return i / 2
}

func buildMaxHeap(array []*Item, heapsize int) {
	var j = heapsize / 2
	for j > -1 {
		MaxHeapify(array, j, heapsize)
		j--
	}
}

// MaxHeapify - places i in its correct position
func MaxHeapify(array []*Item, i int, heapsize int) {
	// get the positions of the children of the node we want to insert
	var left, right, largest = Left(i), Right(i), 0
	// if the left child is smaller than the len of the array and it is also larger than the parent
	// we mark the child as the largest of the two
	if left < heapsize && array[left].key > array[i].key {
		largest = left
	} else {
		largest = i
	}
	if right < heapsize && array[right].key > array[largest].key {
		largest = right
	}
	// if the largest element is not I (i is already in its correct place)
	// we swap the two and heapify again
	if largest != i {
		array[i], array[largest] = array[largest], array[i]
		MaxHeapify(array, largest, heapsize)
	}
}
