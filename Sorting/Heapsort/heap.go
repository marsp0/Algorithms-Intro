// Max heap property - for every node i other than the root
// A[Parent(i)] >= A[i]

// Min heap proprety - for every node i other than the root
// A[Parent(i)] <= A[i]

// Loop invariant : at the start of each iteration of the for loop, the node i+1, i+2 , ... n
// is the root of the max/min heap

// Initialization : prior to the first iteration of the loop, i = floor(n/2). Each node floor(n/2) + 1, floor(n/2) + 2, ... n
// is a leaf and is thus the root of a trivial max heap. This means that the invariant is true prior to the first iteration.

// Maintenance : To see that each iteration maintains the loop invariant, observe that the children of node i are numbered higher than i.
// By the loop invariant, therefore, they are bot roots of max/min heaps.

// Termination : At termination, i = -1. By the loopp invariant, each node 0,1,2,....,n is the root of the max heap.

// Running time of max/min heapify
// T(n) <= T(2n/3) + O(1)

// MASTER THEOREM case 2
//
// F(n) = O(1)
// F(n) = O(n^c * lg^kn) where c = 0 and k = 0
// lg_ba = log_(3/2)1 = 0 => log_ba = c = 0
// T(n) = O(n^log_ba lg^(k+1)n) = O(lgn)

// How did we get T(2/3n) ?
// The question is answered really well here > https://math.stackexchange.com/questions/181022/worst-case-analysis-of-max-heapify-procedure

package main

import (
	"fmt"
	"math/rand"
	"sort"
)

func main() {
	var i int
	var array []int
	for i < 10000000 {
		array = append(array, rand.Int())
		i++
	}
	Heapsort(array)
	fmt.Println(sort.IntsAreSorted(array))
}

// Heapsort - sorts the array in place with the heapsort algorithm
func Heapsort(array []int) {
	var heapsize, i = len(array), len(array) - 1
	buildMaxHeap(array, heapsize)
	for i > 0 {
		array[i], array[0] = array[0], array[i]
		heapsize--
		MaxHeapify(array, 0, heapsize)
		i--
	}
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

func buildMaxHeap(array []int, heapsize int) {
	var j = heapsize / 2
	for j > -1 {
		MaxHeapify(array, j, heapsize)
		j--
	}
}

func buildMinHeap(array []int, heapsize int) {
	var j = heapsize / 2
	for j > -1 {
		MinHeapify(array, j, heapsize)
		j--
	}
}

// MaxHeapify - places i in its correct position
func MaxHeapify(array []int, i int, heapsize int) {
	// get the positions of the children of the node we want to insert
	var left, right, largest = Left(i), Right(i), 0
	// if the left child is smaller than the len of the array and it is also larger than the parent
	// we mark the child as the largest of the two
	if left < heapsize && array[left] > array[i] {
		largest = left
	} else {
		largest = i
	}
	if right < heapsize && array[right] > array[largest] {
		largest = right
	}
	// if the largest element is not I (i is already in its correct place)
	// we swap the two and heapify again
	if largest != i {
		array[i], array[largest] = array[largest], array[i]
		MaxHeapify(array, largest, heapsize)
	}
}

// MinHeapify - min heapifies the array
func MinHeapify(array []int, i int, heapsize int) {
	var left, right, smallest = Left(i), Right(i), 0
	if left < heapsize && array[left] < array[i] {
		smallest = left
	} else {
		smallest = i
	}
	if right < heapsize && array[right] < array[smallest] {
		smallest = right
	}
	if smallest != i {
		array[i], array[smallest] = array[smallest], array[i]
		MinHeapify(array, smallest, heapsize)
	}
}
