package main

import (
	"fmt"
)

func main() {
	var p = Stack{}
	p.Push(3)
	p.Push(21321)
	p.Push(32)
	p.Print()
	p.Pop()
	p.Pop()
	p.Print()
}

// Stack data structure
type Stack struct {
	array []int
}

// Push - pushes an element onto the stack
func (stack *Stack) Push(value int) {
	stack.array = append(stack.array, value)
}

// Pop - pops out an element from the stack
func (stack *Stack) Pop() int {
	var value = stack.array[len(stack.array)-1]
	stack.array = stack.array[:len(stack.array)-1]
	return value
}

// Print - prints the stack to the console.
func (stack *Stack) Print() {
	fmt.Println(stack.array)
}
