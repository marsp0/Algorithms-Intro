import random
import time

def selection(iterable):
	'''python implementation of the selection sort'''
	# O(n^2)
	len_iterable = len(iterable)
	for i in xrange(len_iterable):
		current_min_element = i

		for j in xrange( i+1, len_iterable):

			if iterable[j]  < iterable[current_min_element] :

				current_min_element = j

			iterable[i], iterable[current_min_element] = iterable[current_min_element] , iterable[i]

	return iterable
