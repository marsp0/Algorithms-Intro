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
		#NOTE : REFORMAT THE CODE HERE
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



def heapsort(array):

	p = Heap()
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

	for i in xrange(1000):

		array.append(random.randint(1,10000))

	heapsort(array)