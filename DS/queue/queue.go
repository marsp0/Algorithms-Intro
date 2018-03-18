package main

import (
	"fmt"
	"math/rand"
)

func main() {
	var p = DoubleQueue{}
	var i int
	var result []*Node
	var initial []*Node
	for i < 100 {
		var data = int(rand.Int31())
		var temp = &Node{nil, nil, data, data}
		p.Enqueue(temp)
		initial = append(initial, temp)
		i++
	}
	i = 0
	for i < 100 {
		result = append(result, p.Dequeue())
		i++
	}
	i = 0
	for i < 100 {
		if initial[i] != result[i] {
			fmt.Println("error")
		} else {
			fmt.Printf("%d : %d\n", initial[i].data, result[i].data)
		}
		i++
	}
	fmt.Println(p.head)
	fmt.Println(p.tail)
}

// DoubleQueue datastructure
type DoubleQueue struct {
	head *Node
	tail *Node
}

// Enqueue - adds an element to the queue.
// O(1)
func (queue *DoubleQueue) Enqueue(value *Node) {
	if queue.head == nil {
		queue.head = value
	} else if queue.tail == nil {
		queue.head.next = value
		queue.tail = value
		queue.tail.previous = queue.head
	} else {
		queue.tail.next = value
		value.previous = queue.tail
		queue.tail = value
	}
}

// Dequeue - returns the element at the beginning of the queue.
//
func (queue *DoubleQueue) Dequeue() *Node {
	if queue.head != nil {
		var value = queue.head
		queue.head = value.next
		if queue.head == queue.tail {
			queue.tail = nil
		}
		return value
	}
	return nil
}

// Node - holds the points to the previous and next elements in the Q
type Node struct {
	next     *Node
	previous *Node
	key      int
	data     int
}
