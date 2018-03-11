// Algorithm to find the maximum subarray in a give array.
// For the algorithm to have sense we need to have negative numbers in the array.
// Otherwise the largest sum subarray is the whole array.

package main

import (
	"fmt"
)

func main() {
	var array = []int{-23, 18, 20, -7, 12, 5}
	var sum, _, _ = findMaxSubarray(array, 0, len(array))
	fmt.Println(sum)
}

// bruteForceMaxSubarray - bruteforces all the options in the array. Running time of O(n^2)
func bruteForceMaxSubarray(array []int) {
	var maxCurrentSum = 0
	var maxCurrentI = 0
	var maxCurrentJ = -1
	var i, j int
	for i < len(array) {
		j = i
		var sum = 0
		for j < len(array) {
			sum += array[j]
			if sum > maxCurrentSum {
				maxCurrentSum = sum
				maxCurrentI = i
				maxCurrentJ = j
			}
			j++
		}
		i++
	}
	fmt.Println(maxCurrentSum)
	fmt.Println(maxCurrentI)
	fmt.Println(maxCurrentJ)
}

// findMaxCrossingSubarray - finds the max subarray that is crossing the mid point
// Given that we need the array to cross the midpoint we know that mid will be in the array.
// We start iterating backwards from mid to low and only add elements if the sum is larger than the previous
// We do the same from mid to high and we get a contigous array.
func findMaxCrossingSubarray(array []int, low, mid, high int) (int, int, int) {
	var leftSum = -1 << 63
	var leftIndex int
	var sum = 0
	var i = mid
	for i > low-1 {
		sum += array[i]
		if sum > leftSum {
			leftSum = sum
			leftIndex = i
		}
		i--
	}

	var rightSum = -1 << 63
	var rightIndex int
	sum = 0
	var j = mid + 1
	for j < high {
		sum += array[j]
		if sum > rightSum {
			rightSum = sum
			rightIndex = j
		}
		j++
	}
	return leftSum + rightSum, leftIndex, rightIndex
}

// findMaxSubarray
func findMaxSubarray(array []int, low, high int) (int, int, int) {

	if high-low == 1 {
		return array[low], low, high
	}
	var mid = (low + high) / 2
	fmt.Printf("%d : %d : %d\n", low, mid, high)
	var leftSum, leftLow, leftHigh = findMaxSubarray(array, low, mid)
	var rightSum, rightLow, rightHigh = findMaxSubarray(array, mid, high)
	var crossSum, crossLow, crossHigh = findMaxCrossingSubarray(array, low, mid, high)
	if leftSum >= rightSum && leftSum >= crossSum {
		return leftSum, leftLow, leftHigh
	} else if rightSum >= leftSum && rightSum >= crossSum {
		return rightSum, rightLow, rightHigh
	}
	return crossSum, crossLow, crossHigh
}
