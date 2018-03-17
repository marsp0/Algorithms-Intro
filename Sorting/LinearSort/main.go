package main

import (
	"fmt"
)

func main() {
	var input = []int{3, 6, 6, 5, 2}
	input = CountingSort(input, 6)
	fmt.Println(input)
}

// CountingSort - sorts the array
// we need to know the max value in the array to be able to implement the algorithm.
// Running time is O(n + k)
func CountingSort(input []int, maxValue int) []int {
	var (
		// O(k)
		auxArray = make([]int, maxValue+1)
		// O(n)
		output = make([]int, len(input))
		i      int
		j      int
	)
	// O(n)
	for i < len(input) {
		auxArray[input[i]]++
		i++
	}

	//  One way, but there is comparison here
	// // O(n + k)
	// for j < len(auxArray) {
	// 	var x int
	// 	for x < auxArray[j] {
	// 		output = append(output, j)
	// 		x++
	// 	}
	// 	j++
	// }

	// O(k)
	i = 1
	for i <= maxValue {
		auxArray[i] += auxArray[i-1]
		i++
	}

	// O(n)
	j = len(input) - 1
	for j >= 0 {
		output[auxArray[input[j]]-1] = input[j]
		auxArray[input[j]]--
		j--
	}

	return output
}

func RadixSort(array []int) {

}
