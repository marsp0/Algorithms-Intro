// Loop Invariant - for any array index k
// 1. if first <=  k <= wall, then array[k] <= pivot
// 2. if wall+1 <= k <= current-1, then array[k] > pivot
// 3. if k == last, then array[k] == pivot

// Initialization - prior the the first iteration of the loop, wall = first - 1 and current = first.
// 1. there are no array  between first and wall, and no array between wall + 1 and current - 1.
// this means that the first 2 points of the invariant are satisfied.
// The assignment at the beginning of the Partition function satisfies the third point.

// Maintanence - two outcomes
// 1. the current element is larger than x, then we just increment the current element.
// 2. The current element is smaller than x, then we increment the wall and swap it with the current element.
// In both cases the points of the loop invariant are satisfied.

// Termination - at termination, current element is equal to the last element. Therefore every element in the set is in one of the three entries described
// by the invariant.

// Analysis -

package main

import (
	"fmt"
	"math/rand"
	"sort"
)

func main() {
	// declarations
	var (
		i     int
		array []int
	)

	// Logic
	for i < 100000000 {
		array = append(array, rand.Int())
		i++
	}
	Quicksort(array, 0, len(array)-1)
	fmt.Println(sort.IntsAreSorted(array))
	// fmt.Println(array)
}

// Quicksort - function that performs the quicksort algorithm
func Quicksort(array []int, first, last int) {
	if first < last {
		var pivot = Partition(array, first, last)
		// fmt.Println(array)
		Quicksort(array, first, pivot-1)
		Quicksort(array, pivot+1, last)
	}
}

// Partition - the function partitions the array into three parts :
// 1. array smaller than the pivot
// 2. The pivot (there might be more than one value equal to the pivot)
// 3. array larger than the pivot.
func Partition(array []int, first, last int) int {
	var (
		pivotIndex = last
		pivot      = array[pivotIndex]
		wall       = first - 1
		current    = first
	)
	for current < last {
		if array[current] <= pivot {
			wall++
			array[wall], array[current] = array[current], array[wall]
		}
		current++
	}
	array[wall+1], array[pivotIndex] = array[pivotIndex], array[wall+1]
	return wall + 1
}

// GetPivot returns the index of the pivot.
// The idea of the function is to implement efficient quicksort.
func GetPivot(array []int) int {
	return len(array) - 1
}
