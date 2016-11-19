import random
import time

def selection(iterable):
	'''python implementation of the selection sort'''
	len_iterable = len(iterable)
	for i in xrange(len_iterable):
		current_min_element = i

		for j in xrange( i+1, len_iterable):

			if iterable[j]  < iterable[current_min_element] :

				current_min_element = j

			iterable[i], iterable[current_min_element] = iterable[current_min_element] , iterable[i]

	return iterable


if __name__ == '__main__' :

	data = [random.randint(1,1000) for x in xrange(10000)]
	current_time = time.time()
	data = selection(data)
	after_time = time.time()
	total_time = after_time - current_time
	print total_time