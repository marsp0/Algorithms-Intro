import random
import time

def quicksort(array):
	less_list = []
	pivot_list = []
	more_list = []

	if len(array) <= 1:
		return array
	else:
		pivot_element = array[0]
		for item in array:
			if item < pivot_element:
				less_list.append(item)
			elif item > pivot_element:
				more_list.append(item)
			else:
				pivot_list.append(item)

		less_list = quicksort(less_list)
		more_list = quicksort(more_list)
		return less_list + pivot_list + more_list


if __name__ == '__main__':

	array = []
	for i in xrange(1000000):
		array.append(random.randint(1,100000))
	before = time.time()
	quicksort(array)
	after = time.time()
	print after - before