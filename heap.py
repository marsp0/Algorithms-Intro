''' Implementation of the Heap structure using a dynamic array.

	Basic Idea : data structure that visually is a complete binary tree, but the actual
	structure is an array (doubly linked list)


'''

import time
import random

class Heap(object):

	def __init__(self):
		''' a heap starting from the 1st element and trying to decouple the two functions
			first child is at 2n
			second child is at 2n + 1
		'''
		self.heap = [0]
		self.size = 0

	def insert(self,element):

		self.heap.append(element)
		self.size += 1
		self.bubble_up(self.size)
		return True

	def bubble_up(self,index):
		#reach the top of the heap
		while index // 2 > 0:
			if self.heap[index] < self.heap[index//2]:
				self.heap[index], self.heap[index//2] = self.heap[index//2], self.heap[index]
			index = index // 2
		return True

	def bubble_down(self,index):
		while index*2 <= self.size:
			min_index = self.min_child(index)
			self.heap[index], self.heap[min_index] = self.heap[min_index], self.heap[index]
			index = min_index
		return True

	def min_child(self,index):
		if (index*2 + 1) <= self.size:
			if self.heap[index*2] < self.heap[index*2 + 1]:
				return index*2
			else:
				return index*2 + 1
		else:
			return index*2

	def extract_min(self):

		to_return = self.heap[1]
		self.size -= 1
		if len(self.heap) == 2:
			pass
		else:
			self.heap[1] = self.heap.pop(-1)
			self.bubble_down(1)
		return to_return

	def __len__(self):

		return self.size

''' functions to create heap from an existing array 
	The build function has a complexity of O(n)
'''

def bubble_down(array,index):
	size = len(array)
	while (index*2 + 2) <= size:
		min_index = min_child(array,index)
		if min_index != False:
			array[index], array[min_index] = array[min_index], array[index]
			index = min_index
		else:
			break
	return True

def min_child(array,index):
	size = len(array)
	if (index*2 + 2) < size:
		if array[index*2 + 1] < array[index] or array[index*2 + 2] < array[index]:
			if array[index*2 + 1] < array[index*2 + 2]:
				return (index*2 + 1)
			else:
				return (index*2 + 2)
	else:
		if array[index*2 + 1] < array[index]:
			return (index*2 + 1)
	return False


def build(array):
	size = len(array)
	for i in xrange((size)//2, -1,-1):
		bubble_down(array, i)
	return array

def extract(array):
	if len(array) == 1:
		return	array.pop()
	else:
		to_return = array[0]
		array[0] = array.pop(-1)
		bubble_down(array,0)
	return to_return

def insert(array,element):

	array.append(element)
	bubble_up(array, len(array)-1)
	return True

def bubble_up(array,index):
	while (index - 1)// 2 >= 0:
		if array[index][2] < array[(index - 1)//2][2]:
			array[index], array[(index - 1)//2] = array[(index - 1)//2], array[index]
		index = (index - 1) // 2
	return True


def heapsort(array):
	new_one = []
	build(array)
	before = time.time()
	for index in xrange(len(array)):
		new_one.append(extract(array))
	after = time.time()
	print after - before
	return new_one

if __name__ == '__main__':
	array = []
	for i in xrange(10):

		array.append(random.randint(1, 100000))

	print heapsort(array)