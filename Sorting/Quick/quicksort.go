// Loop Invariant - for any array index k
// 1. if first <=  k <= wall, then array[k] <= pivot
// 2. if wall+1 <= k <= current-1, then array[k] > pivot
// 3. if k == last, then array[k] == pivot

// Initialization - prior the the first iteration of the loop, wall = first - 1 and current = first.
// 1. there are no elements  between first and wall, and no elements between wall + 1 and current - 1.
// this means that the first 2 points of the invariant are satisfied.
// The assignment at the beginning of the Partition function satisfies the third point.

// Maintanence - two outcomes
// 1. the current element is larger than x, then we just increment the current element.
// 2. The current element is smaller than x, then we increment the wall and swap it with the current element.
// In both cases the points of the loop invariant are satisfied.

// Termination - at termination, current element is equal to the last element. Therefore every element in the set is in one of the three entries described
// by the invariant.

package main

import (
	"fmt"
)

func main() {
	var array = []int{13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11}
	Quicksort(array, 0, len(array)-1)
	fmt.Println(array)
}

// Quicksort - function that performs the quicksort algorithm
func Quicksort(array []int, first, last int) {
	if first < last {
		var pivot = Partition(array, first, last)
		// fmt.Printf("%d, %d, %d\n", first, pivot, last)
		Quicksort(array, first, pivot-1)
		Quicksort(array, pivot+1, last)
	}
}

// Partition - the function partitions the array into three parts :
// 1. Elements smaller than the pivot
// 2. The pivot (there might be more than one value equal to the pivot)
// 3. Elements larger than the pivot.
func Partition(array []int, first, last int) int {
	var pivot = array[last]
	var wall, current = first - 1, first
	for current < last {
		if array[current] <= pivot {
			wall++
			array[wall], array[current] = array[current], array[wall]
		}
		current++
	}
	array[wall+1], array[last] = array[last], array[wall+1]
	return wall + 1
}
