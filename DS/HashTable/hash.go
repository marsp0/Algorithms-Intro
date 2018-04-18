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

import (
	"fmt"
	"math/rand"
)

func main() {
	var p = NewDict()
	for i := 0; i < 20; i++ {
		var node = &Node{
			key:      i,
			data:     "32",
			next:     nil,
			previous: nil,
		}
		p.Insert(node)
	}

	for i := 0; i < 10; i++ {
		var t = rand.Intn(20)
		p.Delete(t)
	}
	p.Traverse()
}

// NewDict - initiates a new dict object.
func NewDict() Dict {
	var dict Dict
	dict.count = 0
	dict.size = 7
	dict.array = make([]LinkedList, dict.size)
	return dict
}

// Dict struct that implements a hash table with
// chaining.
type Dict struct {
	count int
	size  int
	array []LinkedList
}

// Insert - insertes a node in the hashtable.
// Expected running time O(1)
// Worst case - O(n) when we have to resize the array.
func (dict *Dict) Insert(node *Node) {
	var (
		index = dict.Hash(node.key)
		val   = dict.Get(node.key)
	)
	if val == nil {
		dict.array[index].Insert(node)
		dict.count++
		if dict.count > dict.size {
			dict.Resize(true)
		}
	}
}

// Get - gets an element from the hashtable in O(1)
func (dict *Dict) Get(key int) *Node {
	return dict.array[dict.Hash(key)].Search(key)
}

// Delete - deletes an element from the has table in O(1)
func (dict *Dict) Delete(key int) {
	var index = dict.Hash(key)
	dict.array[index].Delete(key)
	dict.count--
	if dict.count < dict.size/4 {
		dict.Resize(false)
	}
}

// Resize - responsible for the resizing of the array.
func (dict *Dict) Resize(upwards bool) {
	var (
		currentNode *Node
		newArray    []LinkedList
	)
	if upwards {
		// upsize
		newArray = make([]LinkedList, dict.size*2)
		dict.size *= 2
	} else {
		// downsize
		newArray = make([]LinkedList, dict.size/2)
	}
	for i := 0; i < len(dict.array); i++ {
		currentNode = dict.array[i].head
		for {
			if currentNode == nil {
				break
			} else {
				var (
					index    = dict.Hash(currentNode.key)
					nextNode = currentNode.Next()
				)
				currentNode.next = nil
				currentNode.previous = nil
				newArray[index].Insert(currentNode)
				currentNode = nextNode
			}
		}
	}
	dict.array = newArray
}

// Traverse - traverses the hash table.
func (dict *Dict) Traverse() {
	for i := 0; i < len(dict.array); i++ {
		var currentNode = dict.array[i].head
		for {
			if currentNode == nil {
				break
			} else {
				fmt.Println(currentNode.key)
				var nextNode = currentNode.Next()
				currentNode.next = nil
				currentNode.previous = nil
				currentNode = nextNode
			}
		}
	}
}

// Hash - returns the has value that we are going to use as index
func (dict *Dict) Hash(key int) int {
	if dict.size == 0 {
		return 0
	}
	return key % dict.size
}

// LinkedList - used for the implementation of chaining in hash tables.
type LinkedList struct {
	head *Node
}

// Insert - implements the insertion in the linked list
// Inserting at beginning is O(1) - current
// otherwise is O(n)
// Note :
// Arrays - Indexing is constant time, insertion is linear.
// Linked list - indexing is linear, insertion is constant.
func (list *LinkedList) Insert(value *Node) {
	if list.head != nil {
		list.head.previous = value
		value.next = list.head
		list.head = value
	} else {
		list.head = value
	}
}

// Delete - implements the deletion in linked list.
// Deletion of elements at start is constant time
// Deletion of arbitrary elements is O(n)
func (list *LinkedList) Delete(key int) {
	// declarations
	var (
		sentinel    = true
		currentNode = list.head
	)
	if list.head != nil && list.head.key == key {
		list.head = list.head.Next()
	} else {
		for sentinel {
			if currentNode != nil && currentNode.key != key {
				currentNode = currentNode.Next()
			} else {
				if currentNode != nil {
					if currentNode.previous != nil {
						currentNode.previous.next = currentNode.Next()
					}
					if currentNode.next != nil {
						currentNode.next.previous = currentNode.Previous()
					}
				}
				sentinel = false
			}
		}
	}
}

// Search - searches through the linked list and returns a pointer to the node.
// Linear time.
func (list *LinkedList) Search(key int) *Node {
	var (
		sentinel    = true
		currentNode = list.head
	)

	for sentinel {
		if currentNode.key == key {
			return currentNode
		}
		currentNode = currentNode.Next()
		sentinel = false
	}
	// As always , it is better to return 2 values in GO
	return nil
}

// Node - building block for a linked list.
// contains pointers to previous and next elements.
type Node struct {
	key      int
	data     string
	next     *Node
	previous *Node
}

// Next - returns a pointer to the next node.
func (node *Node) Next() *Node {
	return node.next
}

// Previous - returns a pointer to the previous node.
func (node *Node) Previous() *Node {
	return node.previous
}
