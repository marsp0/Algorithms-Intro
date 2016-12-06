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


	def delete(self,element):

		pass

if __name__ == '__main__':


	p = MinHeap()
	for i in xrange(20, 1, -1):

		p.insert(i)
	
	print p.heap