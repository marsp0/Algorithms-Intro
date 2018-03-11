package main

import (
	"fmt"
	"math/rand"
	"sort"
)

func main() {
	var i int
	var elements []int
	for i < 10 {
		elements = append(elements, rand.Int())
		i++
	}
	InsertionSortDecreasing(elements)
	fmt.Println(sort.IntsAreSorted(elements))
}

/*
Input : A sequence of n numbers [a1, a2, a3, ... , an]
Output : A permutation of the input sequence such that a'1 <= a'2 <= a'3 <= ... <= a'n
*/

// InsertionSort - sorts the sequence of elements using the Insertion Sort algorithm
func InsertionSort(elements []int) {
	// Initiate the starting vars
	var i, j int
	// start looping over the elements in the array (this is where the first n comes from)
	for i < len(elements) {
		j = i
		// in the second loop we basically keep pushing the
		// largest element down the array
		for j > 0 && elements[j-1] > elements[j] {
			elements[j-1], elements[j] = elements[j], elements[j-1]
			j--
		}
		i++
	}
}

// EXERCISES

// InsertionSortDecreasing - sorts in decreasing order
func InsertionSortDecreasing(elements []int) {
	var i, j int
	for i < len(elements) {
		j = i
		for j > 0 && elements[j-1] < elements[j] {
			elements[j-1], elements[j] = elements[j], elements[j-1]
			j--
		}
		i++
	}
}

// Search - performs linear search
func Search(elements []int, val int) {
	var i int
	for i < len(elements) {
		if elements[i] == val {
			fmt.Println("Found it")
			return
		}
	}
	fmt.Println("The value is not in the array")
}
