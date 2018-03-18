// Direct Access Table
// - store items in an array. Index in the array is the actual key.
// CONS :
// 1. Keys can only be integers
// 2. Memory could be a problem
// 		- hash table with 1 element , but its key is 10 000 000.
// 		- We have to initialize an array with 10m elements.

// Solution to CON 1: prehash
// - map keys to nonnegative integers.
//  	- need to make sure that prehash never changes the value of the key.

// Solution to CON 2: hashing
// 	- possible keys are infinite
//  - we have an array with size M
//  - have a function H that takes a key
//  and returns a number k <= M

// Chaining - solution to the collision problem.
// If we have multiple values hasing to the same number,
// then just store all those values in a list at that index

// Hash functions
// 1. Division method
// 		- h(k) = k mod M
//  - bad if M and k have a lot of factors in common.
//  - good if M is prime
//
// 2. Multiplication method
// 		- h(k) = ((a * k) mod 2^w) >> (w - r)
// 		- w - w bit machine (32,64)
// 		- a - random w bit integer. A should be odd and it should not be close to a power of 2
// 		- r - M = 2^r
// 3. Universal hashing
// 		- h(k) = ((ak + b) mod p) mod m
// 		- a and b - random numbers between 0 and p
// 		- p - big prime number

// Open Addressing
package main

func main() {

}

// Item - holds the key and the data associated with a single item
type Item struct {
	key  int
	data string
}

// DATable - implements a direct address table.
type DATable struct {
	array []*Item
}

// NewDATable - returns a new DATable with initialized internal structure.
func NewDATable(size int) DATable {
	var initializedArray = make([]*Item, size)
	var value = DATable{array: initializedArray}
	return value
}

// Search - returns the item at index key to the caller.
// O(1)
func (dat *DATable) Search(key int) *Item {
	return dat.array[key]
}

// Insert - inserts an item in the table - O(1)
func (dat *DATable) Insert(item *Item) {
	dat.array[item.key] = item
}

// Delete - deletes an element from the table.
// O(1)
func (dat *DATable) Delete(key int) {
	dat.array[key] = nil
}
