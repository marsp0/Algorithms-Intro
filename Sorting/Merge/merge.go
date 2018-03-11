package main

import (
	"fmt"
	"math/rand"
	"sort"
)

func main() {
	var i int
	var elements []int
	for i < 10000 {
		elements = append(elements, rand.Int())
		i++
	}
	elements = MergeSort(elements)
	fmt.Println(sort.IntsAreSorted(elements))
}

// MergeSort - performs the merge sort
func MergeSort(array []int) []int {
	if len(array) < 2 {
		return array
	}
	return Merge(MergeSort(array[:len(array)/2]), MergeSort(array[len(array)/2:]))

}

// Merge - merges the two lists
func Merge(left, right []int) []int {
	var newArray []int
	var i, j, k int
	for k < len(left)+len(right) {
		if i < len(left) && i > 0 && j < len(right) && j > 0 {
			if left[i] <= right[j] {
				newArray = append(newArray, left[i])
				i++
			} else if right[j] <= left[j] {
				newArray = append(newArray, right[j])
				j++
			}
		}
		if i > len(left)-1 && j <= len(right)-1 {
			newArray = append(newArray, right[j])
			j++
		}
		if j > len(right)-1 && i <= len(left)-1 {
			newArray = append(newArray, left[i])
			i++
		}
		k++
	}
	return newArray
}
