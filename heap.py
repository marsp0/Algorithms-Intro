''' Implementation of the Heap structure using a dynamic array.

	Basic Idea : data structure that visually is a complete binary tree, but the actual
	structure is an array (doubly linked list)


'''

import time
import random

class MinHeap(object):

	def __init__(self):

		self.heap = []

	def insert(self,element):
		self.heap.append(element)
		if len(self.heap) == 1:
			return
		current_index = len(self.heap) - 1
		while True:
			if current_index % 2 == 1 and current_index != 0:
				if self.heap[current_index] < self.heap[(current_index-1)//2]:
					self.heap[current_index], self.heap[(current_index-1)//2] = self.heap[(current_index-1)//2] , self.heap[current_index]
					current_index = (current_index-1)//2
				else:
					break
			elif current_index % 2 == 0 and current_index != 0:
				if self.heap[current_index] < self.heap[(current_index-1)//2]:
					self.heap[current_index], self.heap[(current_index-1)//2] = self.heap[(current_index-1)//2] , self.heap[current_index]
					current_index = (current_index-2)//2
				else:
					break
			else:
				return
		return

	def extract_min(self):

		to_return = self.heap[0]
		self.heap[0] = self.heap.pop(-1)
		while True:
			if self.heap[0] < self.heap[1] and self.heap[0] < self.heap[2]:
				return to_return
			else:
				if self.heap[1] < self.heap[2]:
					self.heap[0], self.heap[1] = self.heap[1], self.heap[0]
				else:
					self.heap[0], self.heap[2] = self.heap[2], self.heap[0]


def heapsort(array):

	p = MinHeap()
	new_one = []
	for i in array:
		p.insert(i)
	before = time.time()
	for index in xrange(len(array)):

		new_one.append(p.extract_min())
	after = time.time()
	print after - before
	return new_one

if __name__ == '__main__':
	array = []
	for i in xrange(10):

		array.append(random.randint(1,1000))

	print heapsort(array)